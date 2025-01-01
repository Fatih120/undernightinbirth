# because this is the easy lazy fast way, drag+drop

import sys
import os
def extract_dds(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    start_marker = b'\x44\x44\x53\x20\x7C'
    end_marker = b'\x50\x47\x45\x44'
    start = 0
    count = 1
    base_filename, file_extension = os.path.splitext(input_file)
    while True:
        start = data.find(start_marker, start)
        if start == -1:
            break
        end = data.find(end_marker, start)
        if end == -1:
            end = len(data)
        dds_data = data[start:end]
        output_file = f'{base_filename}_{count}.dds'
        with open(output_file, 'wb') as f:
            f.write(dds_data)
        start = end
        count += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.exists(input_file):
            extract_dds(input_file)
        else:
            print("File not found.")
    else:
        print("drag a pat that has ddses here")
