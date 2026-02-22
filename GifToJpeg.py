#!/usr/bin/env python3
"""
GIF to JPEG Batch Converter
===========================

DESCRIPTION
    This Python script provides a simple, interactive batch conversion tool 
    that scans a user-specified source directory ("PullDirectory") for GIF 
    image files and converts each one to standard JPEG (.jpg) format. 
    The converted files are saved to a separate user-specified destination 
    directory while preserving the original base filename.

    Conversion process:
      • Opens the GIF using Pillow (PIL)
      • Converts the image to RGB mode (JPEG does not support transparency/alpha 
        channels or animated frames)
      • Saves the result as a .jpg file in the destination directory

AUTHOR
    Jacob McEvoy

CREATED
    2025

VERSION
    1.0.0

PYTHON REQUIREMENT
    Python 3.6+

DEPENDENCIES
    Pillow (PIL Fork) → install with: pip install Pillow

USAGE
    1. Save this script (e.g., as gif_to_jpeg_converter.py)
    2. Run it in a terminal or command prompt:
         python gif_to_jpeg_converter.py
    3. When prompted, enter the full path to the directory containing your GIF files
    4. When prompted, enter the full path to the destination directory for the JPEGs
    5. Watch the console for real-time progress and results

FEATURES
    • Interactive console prompts for source and destination paths
    • Processes only regular files (ignores subdirectories and folders)
    • Validates file format before conversion (only GIFs are processed)
    • Graceful error handling with clear success/failure messages
    • Preserves original filename (changes only the extension to .jpg)

IMPORTANT NOTES & LIMITATIONS
    • This script is NOT recursive — it only looks at files directly inside 
      the PullDirectory (no subfolders are scanned)
    • Animated GIFs are converted to a static JPEG using only the first frame
    • Existing files in the destination directory with the same name will be overwritten
    • Both directories must already exist and be accessible (read permission 
      on source, write permission on destination)
    • JPEG format does not support transparency or animation
    • Large GIF collections or very large files may take time to process

LICENSE
    Free for personal, educational, and commercial use. 
    Provided "AS IS" without any warranty of any kind.

FEEDBACK / IMPROVEMENTS
    Feel free to modify or extend the script as needed.
"""


from PIL import Image
import os

PullDirectory = input("Directory to pull gif files from: ") # The directory that has the gif files that will be converted to jpeg.
Destination = input("Directory to put jpeg files: ") # The destination directory that will hold the converted jpeg files.

for item in os.listdir(PullDirectory): # For each in the directory given to pull from.

    ItemPath = os.path.join(PullDirectory, item)
    if os.path.isfile(ItemPath): # Check if the item is a file and not a folder.

        with Image.open(ItemPath) as img:
            if img.format == "GIF": # Check if the item is a gif file.
                print(f"Found gif file '{item}' \nAttempting to convert...")
                try: # Attempt to convert from gif to jpeg.
                    img = img.convert("RGB") # "RGB" and not "RGBA" because jpeg does not support transparency.

                    filename = os.path.splitext(os.path.basename(ItemPath))[0] # Get the name of the file without the .extension
                    destinationPath = os.path.join(Destination, filename + ".jpg") # Make the destination path.

                    img.save(destinationPath, "JPEG") # Save image.
                except: # If saving fails... 
                    print(f"Failed to convert '{item}")
                else: # If saving succeeds...
                    print(f"Successfully converted '{item}' to '{destinationPath}'")


