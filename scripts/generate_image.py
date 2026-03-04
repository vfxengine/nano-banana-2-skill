#!/usr/bin/env python3
"""
Nano Banana 2 - Image Generation Script
Generates images from text prompts using Google's Gemini 3.1 Flash Image model (Nano Banana 2).

Usage:
    python generate_image.py "prompt" output.png [--aspect RATIO] [--size SIZE]

Examples:
    python generate_image.py "A cat wearing a wizard hat" cat.png
    python generate_image.py "Futuristic city" city.png --aspect 16:9 --size 4K
"""

import argparse
from utils import check_api_key, import_genai, generate_with_retry, save_image

def main():
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana 2 (Gemini 3.1 Flash Image)")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("output", help="Output file path (e.g., output.png)")
    parser.add_argument("--aspect", default="1:1",
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--size", default="2K",
                        choices=["1K", "2K", "4K"],
                        help="Image resolution (default: 2K)")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model to use (default: gemini-3.1-flash-image-preview)")

    args = parser.parse_args()
    api_key = check_api_key()
    genai, types = import_genai()

    client = genai.Client(api_key=api_key)

    print(f"Generating image: '{args.prompt}'")
    print(f"Settings: aspect={args.aspect}, size={args.size}, model={args.model}")

    response = generate_with_retry(
        client,
        model=args.model,
        contents=[args.prompt],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            image_config=types.ImageConfig(
                aspect_ratio=args.aspect,
                image_size=args.size
            )
        )
    )

    save_image(response, args.output)

if __name__ == "__main__":
    main()
