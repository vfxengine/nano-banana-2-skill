# Nano Banana 2 -- Claude Code Skill

[![Built by VFX Engine](https://img.shields.io/badge/Built%20by-VFX%20Engine-orange)](https://www.vfxengine.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill for image generation, editing, and composition using Google's Gemini 3.1 Flash Image model (Nano Banana 2). Built by [VFX Engine](https://www.vfxengine.com) -- the platform for VFX artists and creators.

## Features

- **Text-to-image generation** with aspect ratio and resolution control (up to 4K)
- **Image editing** with natural language instructions
- **Multi-image composition** -- combine up to 14 reference images
- **Interactive refinement** -- iterative back-and-forth design sessions
- **Search-grounded generation** -- create visuals using real-time data from Google Search
- **Retry logic** with exponential backoff for rate limits and transient errors
- **Blank image detection** -- warns if output looks corrupt or empty

## Installation

### As a Claude Code Skill

```bash
# Clone into your Claude Code skills directory
git clone https://github.com/vfxengine/nano-banana-2-skill.git ~/.claude/skills/nano-banana
```

### Setup

1. Get a [Gemini API key](https://aistudio.google.com/apikey)
2. Set the environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```
3. Install Python dependencies:
   ```bash
   cd ~/.claude/skills/nano-banana
   pip install -r requirements.txt
   ```

## Quick Start

### Generate an Image

```bash
python scripts/generate_image.py "A tabby cat wearing a wizard hat on a moss-covered log in an enchanted forest, 85mm portrait lens, golden hour" cat.png
```

### Edit an Existing Image

```bash
python scripts/edit_image.py photo.png "Add a dramatic sunset to the background" edited.png
```

### Compose Multiple Images

```bash
python scripts/compose_images.py "Create a group photo in an office setting" team.png person1.png person2.png
```

### Interactive Refinement

```bash
python scripts/chat_image.py
> Create a minimalist logo for 'Acme Corp'
> Make the text bolder and add a blue gradient
> save acme_logo.png
```

### Search-Grounded Generation

```bash
python scripts/search_grounded_image.py "Visualize today's weather in Tokyo as an infographic" weather.png --aspect 9:16
```

## Scripts

| Script | Purpose |
|--------|---------|
| `generate_image.py` | Text-to-image generation |
| `edit_image.py` | Edit/modify existing images |
| `compose_images.py` | Combine up to 14 reference images |
| `chat_image.py` | Interactive multi-turn refinement |
| `search_grounded_image.py` | Generate images with real-time search data |

## Options

All scripts support:
- `--aspect` -- Aspect ratio: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- `--size` -- Resolution: `1K` (1024px), `2K`, `4K`
- `--model` -- Override model (default: `gemini-3.1-flash-image-preview`)

```bash
python scripts/generate_image.py "Futuristic motorcycle on Mars" mars.png --aspect 16:9 --size 4K
```

## Prompting Guide

See [PROMPTING.md](PROMPTING.md) for the complete deep-dive guide on writing effective prompts for Nano Banana 2.

**Key principle:** Describe the scene like you're briefing a professional photographer. NB2 has a 32K token context window and understands full natural language, Markdown, and JSON -- not just keyword tags.

```
# Bad
cat, wizard hat, forest, magical, 4k, detailed

# Good
A tabby cat wearing a tiny hand-knitted wizard hat sits on a moss-covered
log in a misty enchanted forest. Soft dappled sunlight filters through
ancient oak trees. Shot on 85mm portrait lens, shallow depth of field,
golden hour lighting, 4K.
```

## License

[MIT](LICENSE)

---

## Built by [VFX Engine](https://www.vfxengine.com)

[VFX Engine](https://www.vfxengine.com) is a platform for VFX artists and creators, featuring generation tools, a visual workflow editor (Studio), production management, and more.

- [Website](https://www.vfxengine.com)
- [Discord](https://discord.gg/zKkWy9YaY8)
- [GitHub](https://github.com/vfxengine)

If you found this skill useful, give it a star!
