# makes images with applied palette onto 0.png in the folder (for sprite sheets)

import os
from PIL import Image

def apply_palette(reference_image_path, palette_image_path, output_path):
    reference_image = Image.open(reference_image_path)
    palette_image = Image.open(palette_image_path)
    if reference_image.mode != 'P' or palette_image.mode != 'P':
        print(f"Error: Both images must be in indexed color mode. Skipping {palette_image_path}")
        return
    palette = palette_image.getpalette()
    new_image = reference_image.copy()
    new_image.putpalette(palette)
    new_image.save(output_path)
    print(f"Saved new image with palette from {palette_image_path}")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    reference_image_path = os.path.join(current_dir, '0.png')
    if not os.path.exists(reference_image_path):
        print(f"Error: Reference image '0.png' not found in {current_dir}")
        return
    output_dir = os.path.join(current_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    for i in range(1, 41):
        palette_image_path = os.path.join(current_dir, f'{i}.png')
        output_path = os.path.join(output_dir, f'0_with_palette_{i}.png')
        if os.path.exists(palette_image_path):
            apply_palette(reference_image_path, palette_image_path, output_path)
        else:
            print(f"Palette image {i}.png not found, skipping")
    
if __name__ == "__main__":
    main()
