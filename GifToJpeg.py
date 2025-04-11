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

                img = img.convert("RGB") # "RGB" and not "RGBA" because jpg does not support transparency.

                filename = os.path.splitext(os.path.basename(ItemPath))[0] # Get the name of the file without the .extension
                destinationPath = os.path.join(Destination, filename + ".jpg") # Make the destination path

                img.save(destinationPath, "JPEG") # Save Image
                print(f"Successfully converted '{item}' to '{destinationPath}'")
