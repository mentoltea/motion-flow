import PIL
from PIL import Image
from definitions import *


def get_pixel_at(img: Image.Image, x:int, y:int) -> Pixel:
    color = img.getpixel((x,y))
    clr = Color(color)
    return Pixel(clr, Point(x,y))

def get_color_at(img: Image.Image, x:int, y:int) -> Color:
    color = img.getpixel((x,y))
    clr = Color(color)
    return clr


def differs(prev: Image.Image, next: Image.Image, x:int, y:int) -> bool:
    pc = get_color_at(prev, x, y)
    nc = get_color_at(next, x, y)
    if ( (pc.r-nc.r)*(pc.r-nc.r) + (pc.g-nc.g)*(pc.g-nc.g) + (pc.b-nc.b)*(pc.b-nc.b) >= 5):
        return True
    return False

def postalg(img: Image.Image) -> Image.Image:
    return img

def alg(prev: Image.Image, next: Image.Image) -> Image.Image:
    (xsize, ysize) = (min(prev.size[0], next.size[0]), min(prev.size[1], next.size[1]))
    img = Image.new("RGB", (xsize, ysize))
    
    for y in range(ysize):
        for x in range(xsize):
            if (differs(prev, next, x, y)):
                img.putpixel((x,y), next.getpixel((x, y)))
    
    img = postalg(img)
    return img        