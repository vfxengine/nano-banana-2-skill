"""
Shared utilities for Nano Banana 2 scripts.
Provides retry logic, error handling, image validation, and common setup.
"""

import os
import sys
import time


def check_api_key():
    """Check for GEMINI_API_KEY and return it, or exit with error."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set", file=sys.stderr)
        print("Get your API key at: https://aistudio.google.com/apikey", file=sys.stderr)
        sys.exit(1)
    return api_key


def import_genai():
    """Import and return (genai, types) modules."""
    try:
        from google import genai
        from google.genai import types
        return genai, types
    except ImportError:
        print("Error: google-genai package not installed.", file=sys.stderr)
        print("Run: pip install google-genai", file=sys.stderr)
        sys.exit(1)


def import_pil():
    """Import and return PIL Image module."""
    try:
        from PIL import Image
        return Image
    except ImportError:
        print("Error: Pillow package not installed.", file=sys.stderr)
        print("Run: pip install Pillow", file=sys.stderr)
        sys.exit(1)


def ensure_output_dir(output_path):
    """Create output directory if it doesn't exist."""
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)


def generate_with_retry(client, max_retries=3, **kwargs):
    """
    Call client.models.generate_content with retry and error handling.
    Retries on rate limits and transient errors with exponential backoff.
    Provides actionable error messages for common failure modes.
    """
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(**kwargs)
        except Exception as e:
            msg = str(e).lower()

            # Rate limiting -- retry with backoff
            if any(term in msg for term in ["rate", "429", "quota", "resource_exhausted"]):
                if attempt < max_retries - 1:
                    wait = 2 ** (attempt + 1)
                    print(f"Rate limited. Retrying in {wait}s... (attempt {attempt + 2}/{max_retries})")
                    time.sleep(wait)
                    continue
                print("Error: Rate limit exceeded. Wait a moment and try again.", file=sys.stderr)
                sys.exit(1)

            # Content blocked by safety filters
            if any(term in msg for term in ["blocked", "safety", "filter", "prohibited"]):
                print("Error: Content was blocked by safety filters.", file=sys.stderr)
                print("Try rephrasing your prompt to avoid restricted content.", file=sys.stderr)
                sys.exit(1)

            # Invalid API key
            if "invalid" in msg and "key" in msg:
                print("Error: Invalid API key. Check your GEMINI_API_KEY.", file=sys.stderr)
                sys.exit(1)

            # Model not found
            if "not found" in msg or "404" in msg:
                print(f"Error: Model not found. It may have been updated or deprecated.", file=sys.stderr)
                print(f"Details: {e}", file=sys.stderr)
                sys.exit(1)

            # Transient error -- retry
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"Error occurred. Retrying in {wait}s... (attempt {attempt + 2}/{max_retries})")
                time.sleep(wait)
                continue

            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


def save_image(response, output_path, min_size_kb=10):
    """
    Extract image from response parts and save to output_path.
    Warns if the image appears blank (< min_size_kb).
    Prints any text parts from the response.
    Exits with error if no image was generated.
    """
    ensure_output_dir(output_path)

    for part in response.parts:
        if part.inline_data:
            image = part.as_image()
            image.save(output_path)

            file_size = os.path.getsize(output_path)
            size_str = f"{file_size / 1024:.1f}KB"

            if file_size < min_size_kb * 1024:
                print(f"Warning: Output is only {size_str} -- it may be blank or corrupt.", file=sys.stderr)
                print("Try rephrasing your prompt or using a different aspect ratio.", file=sys.stderr)

            print(f"Image saved to: {output_path} ({size_str})")
            return True
        elif part.text:
            print(f"Model response: {part.text}")

    print("Error: No image was generated. The model returned only text.", file=sys.stderr)
    print("Try a more specific prompt or different aspect ratio.", file=sys.stderr)
    sys.exit(1)
