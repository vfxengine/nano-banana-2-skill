# Nano Banana 2 (`gemini-3.1-flash-image-preview`) -- Deep Prompting Guide

NB2 delivers Pro-level quality at Flash-level speed, with strong text rendering, character consistency (up to 5 characters / 14 objects), and 4K output. ~37% cheaper than Pro.

**Key difference from older diffusion models**: NB2 has a 32,768-token context window (vs CLIP's 77 tokens). It understands full natural language, Markdown, JSON, and structured instructions. Write like you're briefing a professional photographer, not stuffing tags.

---

## Core Principle: Describe the Scene, Don't List Keywords

A narrative paragraph always beats a keyword list. The model's core strength is deep language understanding.

**Bad**: `cat, wizard hat, forest, magical, 4k, detailed, high quality`
**Good**: `A tabby cat wearing a tiny hand-knitted wizard hat sits on a moss-covered log in a misty enchanted forest. Soft dappled sunlight filters through ancient oak trees. Shot on 85mm portrait lens, shallow depth of field, golden hour lighting, 4K.`

---

## The Universal Prompt Formula

```
[Shot type] + [Subject with details] + [Action/pose] + [Environment/setting] + [Lighting] + [Mood/atmosphere] + [Camera/lens] + [Style] + [Aspect ratio/resolution]
```

Not every element is needed every time -- use what's relevant.

---

## 6 Prompt Archetypes

### 1. Photorealistic Scenes
Think like a photographer. Include camera settings, lighting setup, and physical details.

```
Portrait of an elderly Japanese ceramicist inspecting a tea bowl in a rustic
workshop, illuminated by golden hour light through a window, captured with
85mm portrait lens, soft bokeh, serene mood, vertical orientation.
```

**Photography terms that work well**: wide-angle, macro, 85mm portrait lens, Dutch angle, low-angle perspective, Hasselblad X2D, Canon EOS 90D, Kodak Portra 400 film stock, shallow depth of field, three-point softbox, rim lighting

### 2. Stylized Illustrations & Stickers
Specify the exact art style, color palette, and line treatment.

```
A kawaii-style sticker of a happy red panda wearing a tiny bamboo hat,
munching bamboo leaf, bold clean outlines, cel-shading, vibrant colors,
white background.
```

### 3. Text Rendering (NB2 Strength)
NB2 renders sharp, legible text in multiple languages. Be explicit about typography.

```
Modern minimalist logo for "The Daily Grind" coffee shop with clean
sans-serif font, stylized coffee bean icon integrated with text,
black and white scheme.
```

**Tips**: Put exact text in quotes. Specify font style (serif, sans-serif, bold, italic). Mention placement. NB2 can translate/localize text within images.

### 4. Product Mockups & Commercial Photography
Describe the studio setup like a product photographer would.

```
Studio-lit ceramic coffee mug in matte black on polished concrete,
three-point softbox setup, elevated 45-degree angle, sharp focus on
rising steam, square format.
```

### 5. Minimalist & Negative Space
Leave room for text overlays by specifying negative space.

```
Red maple leaf positioned bottom-right on off-white canvas with
significant empty space, soft diffused top-left lighting, square format.
```

**Tip**: Allocate at least 30% canvas to white space. Use "negative space for text overlay" explicitly.

### 6. Sequential Art (Comics/Storyboards)
Control characters, backgrounds, dialogue, and panel layout.

```
Gritty noir comic panel with detective in trench coat under flickering
streetlamp in rain, neon bar sign reflecting in puddle, caption
"The city was a tough place to keep secrets," harsh dramatic lighting,
landscape format.
```

---

## Advanced Techniques (What Makes NB2 Different)

### Markdown Lists for Structured Instructions
NB2 was trained on code repos and structured docs. Markdown formatting improves adherence:

```
Make ALL of the following edits to the image:
- Change the sky to a dramatic sunset with orange and purple tones
- Add a flock of birds in V-formation
- NEVER add any text or watermarks
- Keep the foreground untouched
```

### ALL CAPS for Critical Requirements
Using CAPS on key words improves adherence: `MUST`, `NEVER`, `EXACTLY`, `ALWAYS`

### Buzzword Composition Enhancement
Professional context descriptors improve quality:
- `Pulitzer-prize-winning cover photo for The New York Times`
- `Vogue editorial spread`
- `National Geographic featured photograph`
- `Apple product launch keynote visual`

### JSON Character Descriptions
For complex characters, provide structured JSON specs. Works better than natural language for precise physical traits because NB2 was trained on code repos and parses structured data natively. Use for character consistency; for general scenes, natural language paragraphs are still superior.

```json
{
  "character": "Detective Sofia",
  "hair": "dark auburn, shoulder-length, slight wave",
  "eyes": "heterochromatic - left green, right amber",
  "build": "athletic, 5'8",
  "outfit": "charcoal trench coat, burgundy scarf, leather boots",
  "distinguishing": "small scar above left eyebrow"
}
```

### Physicality Implication Strategy
Adding physical constraints prevents digital-looking outputs:
- `real-world natural uniform depth of field`
- `natural film grain`
- `subtle lens distortion at edges`

### Negative Instructions (What NOT to Include)
```
Do not include any text, watermarks, or line overlays.
No extra limbs, no text artifacts.
```
But prefer describing what you WANT over what you don't.

### Step-by-Step for Complex Scenes
Break complex requests into sequential steps:
```
First, create a background of a serene, misty forest at dawn.
Then, in the foreground, add a moss-covered ancient stone altar.
Finally, place a single, glowing sword on top of the altar.
```

### Multi-Image Composition Syntax
When composing multiple reference images:
```
the woman [image1] sitting on the chair [image2]
```
Upload clear reference images. Assign distinct names to each character/object.
More references = better consistency (17 refs >> 2 refs).

### Real-Time Search Grounding
Force the model to research before generating:
```
Your plan is to first search for visual references, and generate after.
Create an accurate infographic of today's S&P 500 performance.
```

### Aspect Ratio Control
Be explicit: `16:9 landscape`, `9:16 portrait`, `1:1 square`, `21:9 ultrawide`
If prompting doesn't produce it, provide a reference image with correct dimensions.

### Thinking/Reasoning Mode
NB2 supports configurable thinking levels (High/Dynamic) that let it reason through complex prompts before rendering. Improves quality on multi-constraint prompts.

---

## Category-Specific Prompt Templates

### Cinematic Portrait
```
[Camera] Nikon Z9, 135mm f/1.8
[Subject] Woman in flowing red traditional dress, spinning mid-motion
[Setting] Wheat field at golden hour
[Lighting] Warm backlight with lens flare, rim lighting on dress edges
[Mood] Ethereal, dreamy
[Style] Cinematic film still, slight motion blur on fabric
[Format] 16:9, 4K
```

### Product E-Commerce
```
High-resolution studio photograph of [product] on [surface],
[lighting setup], [camera angle], sharp focus on [detail],
[color palette], negative space on right for text overlay,
[aspect ratio]
```

### Infographic
```
Clean, isometric cutaway illustration of [subject] with distinct
labeled sections showing [data points], modern sans-serif typography,
3-level text hierarchy (headline, subheader, body), white background
with [accent color] nodes, 9:16 portrait format
```

### UI/UX Mockup
```
Mobile app dashboard screen showing [feature], greeting with date,
circular progress ring "[metric]", three stat cards, weekly bar chart,
bottom navigation, rounded corners, soft shadows, dark mode,
DM Sans typography, 9:16
```

### Brand Identity Kit
```
Complete brand identity for "[Brand Name]": primary logo (light/dark
versions), wordmark, color palette with hex values, typography system,
six-icon set, repeating pattern, layout rules, [style adjectives]
on white background
```

### YouTube Thumbnail
```
Reference person with excited surprise expression, pointing right,
[subject] on right side, bold yellow arrow, "[TEXT]" in white with
black outline and red shadow, bright [setting] background, 16:9
```

---

## Editing-Specific Prompts

### Adding/Removing Elements
```
Add a knitted wizard hat to the cat, matching the soft lighting
of the original image.
```

### Inpainting (Targeted Edits)
```
Replace the blue sofa with a vintage brown leather chesterfield.
Keep everything else in the room exactly the same.
```

### Style Transfer
```
Convert this modern city street photo into Vincent van Gogh's
"Starry Night" style with swirling brushstrokes, deep blues,
and bright yellows.
```

### Background Replacement
```
Replace background with photorealistic urban sunset, golden hour,
soft buildings at f/4 equivalent, warm amber/magenta sky,
preserve subject shadows and lighting interaction.
```

### Cinematic Color Grade
```
Apply teal-and-orange color grading, increase contrast, enhance
warm highlights, push shadows to deep teal, slight desaturation
of midtones, Hollywood-quality result, preserve composition.
```

### Localization / Translation
```
Translate all text in this image to Hindi. Adapt the background
setting to Mumbai. Keep the same layout and style.
```

---

## Character Consistency Across Scenes

1. Establish character with rich detail in first prompt
2. Upload clear reference images (more = better; 17 refs >> 2 refs)
3. Assign distinct names: "Sofia the detective", "Max the engineer"
4. In follow-ups, reference by name + key traits
5. NB2 maintains up to 5 characters and 14 objects across a workflow
6. If consistency drifts, restart conversation with full character description

---

## NB2-Specific API Tips

- Model string: `gemini-3.1-flash-image-preview`
- Always include `responseModalities: ['TEXT', 'IMAGE']`
- Iterate through ALL response parts (image may not be first)
- Images return as base64-encoded PNG/JPEG with SynthID watermarks
- Supports 512px to 4K resolution
- Expect 4-6 second generation latency
- Valid 4K PNGs exceed 500KB (blank image check)
- ~$0.039/image at standard resolution

---

## Common Mistakes to Avoid

1. **Keyword soup** -- Write sentences, not tag lists
2. **Vague style** -- "nice" or "good quality" means nothing. Say "photorealistic, shot on Canon 5D Mark IV, f/2.8"
3. **Ignoring lighting** -- Lighting makes or breaks an image. Always specify
4. **No aspect ratio** -- Default may not be what you want. Be explicit
5. **Trying to fix in one shot** -- Use iterative refinement. Edit, don't re-roll
6. **Generic composition** -- Use rule-of-thirds, leading lines, negative space explicitly
7. **Over-specifying negatives** -- Describe what you want, not what you don't

---

## Sources

- [Google Developers Blog: How to Prompt Gemini 2.5 Flash Image Generation](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/)
- [Google DeepMind: Nano Banana 2 (Gemini 3.1 Flash Image)](https://deepmind.google/models/gemini-image/flash/)
- [Google Cloud: Gemini Image Generation Best Practices](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/gemini-image-generation-best-practices)
- [Max Woolf: Nano Banana Prompt Engineering (Advanced)](https://minimaxir.com/2025/11/nano-banana-prompts/)
- [DEV Community: Nano-Banana Pro Prompting Guide & Strategies](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n)
- [ImagineArt: Nano Banana 2 Prompt Guide (50 Examples)](https://www.imagine.art/blogs/nano-banana-2-prompt-guide)
- [AI SuperHub: 50+ Image Prompts Guide](https://www.aisuperhub.io/blog/prompt-engineering-for-gemini-25-flash-image-nano-banana-50plus-image-prompts-included)
- [Google Blog: Build with Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/)
- [LaoZhang AI: Gemini 3.1 Flash Image Complete Guide](https://blog.laozhang.ai/en/posts/gemini-3-1-flash-image-preview)

---

*Built by [VFX Engine](https://www.vfxengine.com) -- the platform for VFX artists and creators. [Website](https://www.vfxengine.com) | [Discord](https://discord.gg/zKkWy9YaY8) | [GitHub](https://github.com/vfxengine)*
