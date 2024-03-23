# This converts RIFF palette files to PNGs, turning the index map
# into a 256-colour table that you'd use in UNIB.
# As far as I know, this is only useful for if you want to convert
# palettes from older Melty Blood games, which have been extracted
# and posted to The Spriter's Resource under PS2, but not as PNGs.
# This should do the work for you and give you your 36 colours.
# Feel free to edit it for other palette formats. Maybe I'll turn
# this into a gist, but I don't know what other purposes you'd use it.

# Many thanks to the contributors of the wiki here: https://worms2d.info/Palette_file

# TRANSPARENCY : Done by AI.

import os
from PIL import Image

def riff_to_png(input_file, output_file):
    colors = []
    
    with open(input_file, 'rb') as f: 
        riff = f.read(4).decode('utf-8') # Riff header
        dataSize = int.from_bytes(f.read(4), byteorder='little')
        type = f.read(4).decode('utf-8')

        chunkType = f.read(4).decode('utf-8') # Chunk reads
        chunkSize = int.from_bytes(f.read(4), byteorder='little')
        palVersion = int.from_bytes(f.read(2), byteorder='little')
        palEntries = int.from_bytes(f.read(2), byteorder='little')

        for i in range(palEntries): # Colour reads
            red = int.from_bytes(f.read(1), byteorder='little')
            green = int.from_bytes(f.read(1), byteorder='little')
            blue = int.from_bytes(f.read(1), byteorder='little')
            flags = int.from_bytes(f.read(1), byteorder='little')

            colors.append((red, green, blue)) # Add colour to list

    img = Image.new('P', (palEntries, 1)) # 8bit image
    img.putdata(list(range(palEntries))) # Set pixels to index
    img.putpalette(sum(colors, ())) # Set image contents to palette

    img.save(output_file, 'PNG')

def convert_pals():
    for file in os.listdir():
        if file.endswith(".pal"):
            input_file = file
            output_file = os.path.splitext(file)[0] + ".png"
            riff_to_png(input_file, output_file)

if __name__ == "__main__":
    convert_pals()
