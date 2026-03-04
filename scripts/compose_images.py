#!/usr/bin/env python3
"""
Nano Banana 2 - Multi-Image Composition Script
Combines multiple reference images into a new composition using Gemini 3.1 Flash Image (Nano Banana 2).

Usage:
    python compose_images.py "prompt" output.png image1.png [image2.png ...]

Examples:
    python compose_images.py "Create a group photo of these people in an office" team.png person1.png person2.png person3.png
    python compose_images.py "Combine these products into a promotional banner" banner.png product1.png product2.png
    python compose_images.py "Create a character sheet with these poses" sheet.png pose1.png pose2.png pose3.png

Note: Supports up to 14 reference images.
"""

import argparse
import os
import sys
from utils import check_api_key, import_genai, import_pil, generate_with_retry, save_image

def main():
    parser = argparse.ArgumentParser(description="Compose multiple images with Nano Banana 2 (Gemini 3.1 Flash Image)")
    parser.add_argument("prompt", help="Composition instruction")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("images", nargs="+", help="Input image files (up to 14)")
    parser.add_argument("--aspect", default="1:1",
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Output aspect ratio (default: 1:1)")
    parser.add_argument("--size", default="2K",
                        choices=["1K", "2K", "4K"],
                        help="Image resolution (default: 2K)")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model to use (default: gemini-3.1-flash-image-preview)")

    args = parser.parse_args()

    if len(args.images) > 14:
        print("Error: Maximum 14 reference images supported", file=sys.stderr)
        sys.exit(1)

    for img_path in args.images:
        if not os.path.exists(img_path):
            print(f"Error: Input file not found: {img_path}", file=sys.stderr)
            sys.exit(1)

    api_key = check_api_key()
    genai, types = import_genai()
    Image = import_pil()

    client = genai.Client(api_key=api_key)

    loaded_images = [Image.open(path) for path in args.images]

    print(f"Composing {len(loaded_images)} images")
    print(f"Instruction: '{args.prompt}'")
    print(f"Settings: aspect={args.aspect}, size={args.size}")

    contents = [args.prompt] + loaded_images

    response = generate_with_retry(
        client,
        model=args.model,
        contents=contents,
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
