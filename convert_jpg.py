from pathlib import Path
from PIL import Image

downscale = 2
for f in Path("./assets/images").glob("*.png"):
    fname = f.parts[-1].split('.')[0]
    npath = Path(*f.parts[:-1], f"{fname}.jpg")
    image = Image.open(f).convert("RGB")
    width, height = image.size
    image = image.resize((width // downscale, height // downscale), Image.Resampling.BICUBIC)
    image.save(npath)
    