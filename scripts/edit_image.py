#!/usr/bin/env python3
"""
Nano Banana 2 - Image Editing Script
Edits existing images based on text prompts using Google's Gemini 3.1 Flash Image model (Nano Banana 2).

Usage:
    python edit_image.py input.png "editing instruction" output.png

Examples:
    python edit_image.py photo.png "Add a sunset to the background" edited.png
    python edit_image.py portrait.png "Remove the background" nobg.png
    python edit_image.py logo.png "Make the text bolder and add blue gradient" logo_v2.png
"""

import argparse
import os
import sys
from utils import check_api_key, import_genai, import_pil, generate_with_retry, save_image

def main():
    parser = argparse.ArgumentParser(description="Edit images with Nano Banana 2 (Gemini 3.1 Flash Image)")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("prompt", help="Editing instruction")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("--aspect", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Output aspect ratio (default: preserve original)")
    parser.add_argument("--size", default=None,
                        choices=["1K", "2K", "4K"],
                        help="Image resolution (default: preserve original)")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model to use (default: gemini-3.1-flash-image-preview)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    api_key = check_api_key()
    genai, types = import_genai()
    Image = import_pil()

    client = genai.Client(api_key=api_key)
    img = Image.open(args.input)

    print(f"Editing image: '{args.input}'")
    print(f"Instruction: '{args.prompt}'")

    image_config_kwargs = {}
    if args.aspect:
        image_config_kwargs['aspect_ratio'] = args.aspect
    if args.size:
        image_config_kwargs['image_size'] = args.size

    config_kwargs = {'response_modalities': ['TEXT', 'IMAGE']}
    if image_config_kwargs:
        config_kwargs['image_config'] = types.ImageConfig(**image_config_kwargs)

    response = generate_with_retry(
        client,
        model=args.model,
        contents=[args.prompt, img],
        config=types.GenerateContentConfig(**config_kwargs)
    )

    save_image(response, args.output)

if __name__ == "__main__":
    main()
