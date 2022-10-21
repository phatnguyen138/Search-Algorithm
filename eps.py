import os,glob
import time
from PIL import Image

def png_generate(path):
    TARGET_BOUNDS = (1024, 1024)
    
    # Change the directory
    os.chdir(path)
    
    # iterate through all file
    for filename in os.listdir():
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
        pic.save(path+filename+".png")

def gif_gene(path):
    frames = []
    imgs = glob.glob(path+"png-file/*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save('png_gif.gif', format='GIF',

                append_images=frames[1:],
                save_all=True, loop=0)