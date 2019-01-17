from convolution import convolution
from PIL import Image
import numpy as np

sharpen = [0, -1, 0, -1, 5, -1, 0, -1, 0]
                
if __name__ == "__main__":
    im = Image.open("ressources/orig.png")
    new = im.convert('LA')
    vec = list(new.getdata())
    new.show()
    l = [x[0] for x in vec] 
    res = convolution(l, sharpen)
    newl = [(x, x, x) for x in res]
    im2 = Image.new(im.mode, im.size)
    im2.putdata(newl)
    im2.show()