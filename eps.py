import os,glob
from PIL import Image

os.chdir("output")

TARGET_BOUNDS = (1024, 1024)

for rootfolder in os.listdir():
    os.chdir(rootfolder)
    # iterate through all file
    for folder in os.listdir():
        os.chdir(folder)
        for filename in glob.glob("*.eps"):
            print(filename)
            pic = Image.open(filename)
            pic.load(scale=10)

            # Ensure scaling can anti-alias by converting 1-bit or paletted images
            if pic.mode in ('P', '1'):
                pic = pic.convert("RGB")

            # Calculate the new size, preserving the aspect ratio
            ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                        TARGET_BOUNDS[1] / pic.size[1])
            new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

            # Resize to fit the target size
            pic = pic.resize(new_size, Image.ANTIALIAS)

            # Save to PNG
            name_file = filename.split(".")[0]
            pic.save(name_file+".jpg")
            os.remove(filename)
        os.chdir('..')
    os.chdir(folder)
