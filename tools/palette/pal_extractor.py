# extracts palettes from dfci, unib, etc
# might end up being wonky and incorrect but it is a start

import sys
from PIL import Image
import os

def read_palette_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def extract_palettes(data):
    palettes = []
    palette_size = 1024
    for i in range(4, len(data), palette_size):
        if i + palette_size <= len(data):
            palette = data[i:i+palette_size]
            palettes.append(palette)
    return palettes

def create_palette_image(palette_data):
    rgb_palette = [palette_data[i:i+3] for i in range(0, len(palette_data), 4)]
    img = Image.new('P', (16, 16))
    img.putpalette(b''.join(rgb_palette))
    img.putdata(range(256))
    return img

def save_palettes(palettes, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for i, palette in enumerate(palettes):
        img = create_palette_image(palette)
        img.save(os.path.join(output_dir, f'{i}.png'))
        print(f'Saved {i}.png')

def main(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = f'{base_name}_palettes'
    data = read_palette_file(file_path)
    palettes = extract_palettes(data)
    save_palettes(palettes, output_dir)
    print(f'Extracted {len(palettes)} palettes.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_palette_file>")
        sys.exit(1)
    
    main(sys.argv[1])
