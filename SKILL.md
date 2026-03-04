---
name: nano-banana
description: Generate, edit, and compose images using Google's Gemini 3.1 Flash Image model (Nano Banana 2). Use this skill when the user asks to create images, generate visuals, edit photos, compose multiple images, create logos, thumbnails, infographics, product shots, or any image generation task. Supports text-to-image, image editing, multi-image composition (up to 14 images), iterative refinement, aspect ratio control, and Google Search-grounded image generation for real-time data visualization.
---

# Nano Banana 2

Image generation skill powered by Google's Gemini 3.1 Flash Image model (Nano Banana 2). Enables text-to-image generation, image editing, multi-image composition, and real-time data visualization. Pro-level quality at Flash-level speed.

**Default model**: `gemini-3.1-flash-image-preview` (Nano Banana 2). Use this unless the user specifically requests Pro or an upgraded model is available.

## Requirements

- `GEMINI_API_KEY` environment variable set
- Python packages: `google-genai`, `Pillow`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Generate an Image

```bash
python scripts/generate_image.py "A cat wearing a wizard hat" cat.png
```

### Edit an Existing Image

```bash
python scripts/edit_image.py photo.png "Add a sunset to the background" edited.png
```

### Compose Multiple Images

```bash
python scripts/compose_images.py "Create a group photo in an office" team.png person1.png person2.png
```

## Available Scripts

| Script | Purpose |
|--------|---------|
| `generate_image.py` | Text-to-image generation |
| `edit_image.py` | Edit/modify existing images |
| `compose_images.py` | Combine up to 14 reference images |
| `chat_image.py` | Interactive multi-turn refinement |
| `search_grounded_image.py` | Generate images with real-time search data |
| `utils.py` | Shared retry logic, error handling, blank image detection |

## Generation Options

### Aspect Ratios
`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`

### Resolutions
`1K` (1024px), `2K` (default), `4K`

### Usage with Options

```bash
python scripts/generate_image.py "Futuristic motorcycle on Mars" mars.png --aspect 16:9 --size 4K
```

### Override Model (for Pro when needed)

```bash
python scripts/generate_image.py "prompt" out.png --model gemini-3-pro-image-preview
```

## Task Workflows

### Logo Generation

```bash
python scripts/generate_image.py "Clean black-and-white logo with text 'Daily Grind', sans-serif font, coffee bean icon, minimalist style" logo.png --aspect 1:1
```

### Product Mockup

```bash
python scripts/generate_image.py "Studio-lit product photo on polished concrete, 3-point softbox, 45-degree angle, professional e-commerce style" product.png --aspect 4:3 --size 4K
```

### Photorealistic Portrait

```bash
python scripts/generate_image.py "A photorealistic close-up portrait, shot on 85mm lens, golden hour lighting, shallow depth of field, cinematic" portrait.png --size 4K
```

### Stylized Art (Anime/Sticker)

```bash
python scripts/generate_image.py "A kawaii red panda sticker, bold outlines, cel-shading, white background, cute expression" sticker.png
```

### Iterative Design Refinement

Use the chat script for back-and-forth refinement:

```bash
python scripts/chat_image.py
```

Then interact:
```
> Create a logo for 'Acme Corp'
[Image generated]
> Make the text bolder and add a blue gradient
[Refined image]
> save acme_logo.png
```

### Real-Time Data Visualization

Generate infographics with current data:

```bash
python scripts/search_grounded_image.py "Visualize today's weather in Tokyo as an infographic" tokyo_weather.png --aspect 9:16
```

Use cases:
- Live stock-market infographics
- Breaking-news visuals
- Weather dashboards
- Current event visualizations

### Multi-Image Composition

Combine reference images:

```bash
python scripts/compose_images.py "Create a product comparison shot with these items side by side, professional lighting" comparison.png item1.png item2.png item3.png --aspect 16:9
```

Use cases:
- Product comparison shots
- Character sheets
- Team photos
- Style-consistent image series

## Inline Python Usage

For integration in larger scripts:

```python
import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=["A serene mountain landscape at dawn"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="2K"
        )
    )
)

for part in response.parts:
    if part.inline_data:
        image = part.as_image()
        image.save("landscape.png")
```

### Editing with Inline Code

```python
from PIL import Image
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
img = Image.open("input.png")

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=["Add dramatic clouds to the sky", img],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)
```

## Prompting Guide

See `PROMPTING.md` for the complete deep-dive prompting guide. Key highlights:

### Core Principle
**Describe the scene, don't list keywords.** NB2 has a 32K token context window and understands full natural language, Markdown, and JSON.

### Universal Prompt Formula
```
[Shot type] + [Subject] + [Action/pose] + [Environment] + [Lighting] + [Mood] + [Camera/lens] + [Style] + [Aspect ratio/resolution]
```

### Power Techniques

**Markdown lists** for multi-edit instructions (trained on code repos):
```
Make ALL of the following edits:
- Change sky to sunset
- Add birds in V-formation
- NEVER add watermarks
```

**ALL CAPS** for critical requirements: `MUST`, `NEVER`, `EXACTLY`

**Buzzword composition**: `Pulitzer-prize-winning cover photo for The New York Times`

**JSON character specs** for complex characters with precise traits

**Physicality constraints** to force photorealism: `real-world natural uniform depth of field`

**Step-by-step** for complex scenes: `First... Then... Finally...`

### Photography Terms That Work
wide-angle, macro, 85mm portrait lens, Dutch angle, Hasselblad X2D, Canon EOS 90D, Kodak Portra 400, shallow depth of field, three-point softbox, rim lighting, golden hour

### NB2 Strengths
- Sharp text rendering in multiple languages (put text in quotes)
- Character consistency (up to 5 chars / 14 objects)
- Search-grounded generation for real-time data
- 512px to 4K resolution
- ~$0.039/image

### Common Mistakes
1. Keyword soup -- write sentences
2. Vague style -- specify camera, lens, settings
3. Ignoring lighting -- always specify
4. No aspect ratio -- be explicit
5. Re-rolling instead of editing -- use iterative refinement
