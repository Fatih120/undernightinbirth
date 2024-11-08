import os
from PIL import Image

# Set the working directory
working_dir = os.getcwd()
print(f"Working directory set to: {working_dir}")

# Get a list of all PNG files in the working directory
png_files = [f for f in os.listdir(working_dir) if f.endswith('.png')]

# Sort the list of files in alphabetical order
png_files.sort()

print(f"Found {len(png_files)} PNG files in the working directory.")

# Set the canvas size
canvas_size = (2048, 2048)
print(f"Canvas size set to {canvas_size[0]}x{canvas_size[1]} pixels.")

# Initialize the current canvas and position
current_canvas = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
current_x = 0
current_y = 0
canvas_count = 1
print("Created the first canvas.")

# Loop through the PNG files and add them to the canvases
for png_file in png_files:
    # Load the PNG image
    png_image = Image.open(os.path.join(working_dir, png_file))

    # Add a 1-pixel black border to the image
    bordered_image = Image.new('RGBA', (png_image.width + 2, png_image.height + 2), (0, 0, 0, 255))
    bordered_image.paste(png_image, (1, 1))

    # Align the image to the nearest multiple of 16 pixels
    aligned_x = (current_x // 16) * 16
    aligned_y = (current_y // 16) * 16

    # Check if the image will fit on the current canvas
    if aligned_x + bordered_image.width > canvas_size[0] or aligned_y + bordered_image.height > canvas_size[1]:
        # If not, save the current canvas and start a new one
        print(f"Current canvas {canvas_count} is full, saving and starting a new one.")
        current_canvas.save(f'canvas_{canvas_count}.png')
        current_canvas = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
        current_x = 0
        current_y = 0
        canvas_count += 1
        print(f"Created canvas {canvas_count}.")
        aligned_x = 0
        aligned_y = 0

    # Add the bordered image to the current canvas
    print(f"Adding image {png_file} to canvas {canvas_count}.")
    current_canvas.paste(bordered_image, (aligned_x, aligned_y))

    # Update the current position
    current_x = aligned_x + bordered_image.width
    if current_x + bordered_image.width > canvas_size[0]:
        current_x = 0
        current_y = aligned_y + bordered_image.height

# Save the final canvas
print(f"Saving final canvas {canvas_count}.")
current_canvas.save(f'canvas_{canvas_count}.png')
