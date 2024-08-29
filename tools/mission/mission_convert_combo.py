import sys
import os
import struct

def parse_input(byte1, byte2):
    faces = {0: '', 1: 'A', 2: 'B', 4: 'C', 6: 'BC', 8: 'D', 9: 'AD'}
    stick = {
        0: '5', 1: '1', 2: '2', 3: '3', 4: '4',
        6: '6', 7: '7', 8: '8', 9: '9'
    }
    
    face = faces.get(byte1, 'X')
    direction = stick.get(byte2, 'X')
    
    return f"{direction}{face}"

def input_to_bytes(input_str):
    direction_to_byte = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 0, '6': 6, '7': 7, '8': 8, '9': 9}
    button_to_byte = {'': 0, 'A': 1, 'B': 2, 'C': 4, 'D': 6}
    
    direction = input_str[0]
    button = input_str[1:] if len(input_str) > 1 else ''
    
    return button_to_byte.get(button, 0), direction_to_byte.get(direction, 0)

def parse_replay(input):
    output_path = os.path.splitext(input)[0] + '.txt'
    
    with open(input, 'rb') as f:
        header = f.read(12)
        frame_count = struct.unpack('<I', header[8:12])[0]  # Last 4 bytes of header
        input_data = f.read()
    
    frames = []
    for i in range(0, min(len(input_data), frame_count * 2), 2):
        if i + 1 < len(input_data):
            frame = parse_input(input_data[i], input_data[i + 1])
            frames.append(frame)
    
    with open(output_path, 'w') as f:
        for frame in frames:
            f.write(f"{frame}\n")
    
    print(f"Replay stream written to {output_path}")
    print(f"Total frames in header: {frame_count} / Actual frames: {len(frames)}")

def dat_out(input):
    output_path = os.path.splitext(input)[0] + '.dat'
    
    with open(input, 'r') as f:
        inputs = [line.strip() for line in f if line.strip()]
    
    frame_count = len(inputs)
    
    with open(output_path, 'wb') as f:
        f.write(struct.pack('<III', 1, 8, frame_count)) #header
        for input_str in inputs: #combo
            button, direction = input_to_bytes(input_str)
            f.write(struct.pack('BB', button, direction))
        padding = 400 - (12 + frame_count * 2)  # padding (useless)
        if padding > 0:
            f.write(b'\x00' * padding)
    
    print(f"Created {output_path}")
    print(f"{frame_count} frames")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = sys.argv[1]
        if os.path.exists(input):
            if input.endswith('.dat'):
                parse_replay(input)
            elif input.endswith('.txt'):
                dat_out(input)
            else:
                print("Error: Input file must be either .dat or .txt")
        else:
            print(f"Error: File '{input}' not found.")
    else:
        print("Drag and drop a .dat or .txt file into this script.")
        sys.exit(1)
