import datetime
import os

from PIL import Image, ImageFile 

def image_add_origin(image, folder):
    data = str(datetime.datetime.now()).replace(" ", "")
    image = Image.open(image.file)
    
    path_image = f'{folder}/{data}.webp'
    image.save(path_image, format='Webp', quality=100, optimize=True)
    return path_image