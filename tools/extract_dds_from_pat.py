# Exports .DDS files from .PAT files, somewhat.
# TRANSPARENCY : This was mostly done by AI so it is messy. Forgive me.
# Non-Issues: Doesn't deal with weirdly-formatted DDS files that would be the same if you manually extracted them 
# To-do: Injector, determine format in filename
# Acts upon all pats in working directory.

import os

def extract_dds_from_pat(pat_path):
    with open(pat_path, 'rb') as file: # RW mode
        data = file.read()
        
    header = b'\x44\x44\x53\x20\x7C'  # DDS |
    terminator = b'\x50\x47\x45\x44'  # PGED, standard for how UNI does it but this might be horrible
    start = 0
    
    while True:
        start = data.find(header, start) # find header
        
        if start == -1:
            break

        # get filename lazily
        filename_start = data.rfind(b'PGNM', 0, start)
        if filename_start != -1:
            filename_end = data.find(b'\x00', filename_start + 4)

            # byte to string
            if filename_end != -1:
                dds_filename = data[filename_start + 4:filename_end].decode('utf-8')
            else:
                # use pat name if not found
                dds_filename = os.path.splitext(os.path.basename(pat_path))[0]
        else:
            # again lol
            dds_filename = os.path.splitext(os.path.basename(pat_path))[0]

        # find PGED
        end = data.find(terminator, start)
        if end == -1:
            # assume EOF
            end = len(data)

        dds_data = data[start:end] # extract
        
        # save beside the pat
        with open(os.path.splitext(pat_path)[0] + "_" + str(start) + ".dds", 'wb') as dds_file:
            dds_file.write(dds_data)
            
        # telling the user what's happening is ALWAYS good
        print(dds_filename + " extracted from " + pat_path + " @ " + str(start))
        start = end

    print(dds_filename + " done.") # yippee

def recurser(directory_path):
    for file in os.listdir(directory_path):
        if file.endswith(".pat"):
            extract_dds_from_pat(os.path.join(directory_path, file))
        elif os.path.isdir(file):
            recurser(os.path.join(directory_path, file))

recurser(".")
