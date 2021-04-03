# Move and rename all .png files on your Desktop
from pathlib import Path

# Identify all screenshots on your Desktop
path = Path().home() / 'Desktop'
screens = [f for f in path.iterdir() if f.suffix == '.png']

# Create a new directory
path.joinpath('images').mkdir()

# Move and rename all screenshots
for i, s in enumerate(screens):
    new_name = f"Pic-{i:0>5}{s.suffix}"
    s.replace(path.joinpath('images', new_name))
