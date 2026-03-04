#!/usr/bin/env python3
"""
Nano Banana 2 - Interactive Chat-Style Image Generation
Creates and iteratively refines images through multi-turn conversation.

Usage:
    python chat_image.py

This script starts an interactive session where you can:
1. Generate an initial image with a prompt
2. Refine the image with follow-up instructions
3. Save any version you like
4. Continue iterating until satisfied

Commands during chat:
    save <filename>  - Save current image
    reset            - Start fresh
    quit/exit        - Exit the session
"""

import os
import sys
import time

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set", file=sys.stderr)
        print("Get your API key at: https://aistudio.google.com/apikey", file=sys.stderr)
        sys.exit(1)

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("Error: google-genai package not installed. Run: pip install google-genai", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    current_image = None
    iteration = 0

    print("=" * 60)
    print("Nano Banana 2 - Interactive Image Generation")
    print("=" * 60)
    print("\nCommands:")
    print("  save <filename>  - Save current image")
    print("  reset            - Start fresh")
    print("  quit/exit        - Exit")
    print("\nEnter your prompt to begin:\n")

    def create_chat():
        return client.chats.create(
            model="gemini-3.1-flash-image-preview",
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )

    chat = create_chat()

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        # Handle commands
        if user_input.lower() in ('quit', 'exit'):
            print("Goodbye!")
            break

        if user_input.lower() == 'reset':
            chat = create_chat()
            current_image = None
            iteration = 0
            print("Session reset. Enter a new prompt to begin.")
            continue

        if user_input.lower().startswith('save '):
            filename = user_input[5:].strip()
            if current_image:
                output_dir = os.path.dirname(filename)
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                current_image.save(filename)
                file_size = os.path.getsize(filename)
                print(f"Image saved to: {filename} ({file_size / 1024:.1f}KB)")
            else:
                print("No image to save. Generate one first.")
            continue

        # Send prompt to Gemini with retry
        iteration += 1
        print(f"\n[Iteration {iteration}] Generating...")

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = chat.send_message(user_input)

                for part in response.parts:
                    if part.inline_data:
                        current_image = part.as_image()
                        print(f"Image generated! Use 'save <filename>' to save it.")
                    elif part.text:
                        print(f"Model: {part.text}")

                break  # Success
            except Exception as e:
                msg = str(e).lower()
                if any(term in msg for term in ["rate", "429", "quota", "resource_exhausted"]):
                    if attempt < max_retries - 1:
                        wait = 2 ** (attempt + 1)
                        print(f"Rate limited. Retrying in {wait}s...")
                        time.sleep(wait)
                        continue
                    print(f"Error: Rate limit exceeded. Wait a moment and try again.")
                elif any(term in msg for term in ["blocked", "safety", "filter"]):
                    print(f"Error: Content blocked by safety filters. Try rephrasing.")
                else:
                    if attempt < max_retries - 1:
                        wait = 2 ** attempt
                        print(f"Error occurred. Retrying in {wait}s...")
                        time.sleep(wait)
                        continue
                    print(f"Error: {e}")
                break

        print()  # Blank line for readability

if __name__ == "__main__":
    main()
