def enhance_promt(promt: str, style: str):
    styles = {
        "realistic": "highly detailed, photorealistic, 8k resolution, intricate details, sharp focus",
        "anime": "anime style, vibrant colors, dynamic composition, expressive characters",
        "fantasy": "epic fantasy art, mystical elements, dramatic lighting, imaginative scenery",
        "cyberpunk": "cyberpunk aesthetic, neon lights, futuristic cityscape, high contrast",
        "pixar": "Pixar style, bright colors, whimsical characters, playful environment",
    }

    return f"{promt} , {styles.get(style, '')}"