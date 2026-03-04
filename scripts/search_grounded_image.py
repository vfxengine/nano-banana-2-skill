#!/usr/bin/env python3
"""
Nano Banana 2 - Google Search-Grounded Image Generation
Creates images using real-time data from Google Search.

Usage:
    python search_grounded_image.py "prompt" output.png [--aspect RATIO] [--size SIZE]

Examples:
    python search_grounded_image.py "Visualize today's weather in Tokyo as an infographic" weather.png
    python search_grounded_image.py "Create an infographic of current Bitcoin price trends" btc.png --aspect 16:9
    python search_grounded_image.py "Illustrate the latest news about AI" ai_news.png --size 2K

This enables:
- Live stock-market infographics
- Breaking-news visuals
- Real-time event visualizations
- Weather dashboards
- Current data visualizations
"""

import argparse
from utils import check_api_key, import_genai, generate_with_retry, save_image

def main():
    parser = argparse.ArgumentParser(description="Generate search-grounded images with Nano Banana 2 (Gemini 3.1 Flash Image)")
    parser.add_argument("prompt", help="Text prompt (can reference current/real-time data)")
    parser.add_argument("output", help="Output file path")
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

    print(f"Generating search-grounded image: '{args.prompt}'")
    print(f"Settings: aspect={args.aspect}, size={args.size}")
    print("Searching for real-time data...")

    response = generate_with_retry(
        client,
        model=args.model,
        contents=[args.prompt],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            image_config=types.ImageConfig(
                aspect_ratio=args.aspect,
                image_size=args.size
            ),
            tools=[{"google_search": {}}]
        )
    )

    save_image(response, args.output)

if __name__ == "__main__":
    main()
