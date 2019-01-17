from convolution import convolution
from PIL import Image
import numpy as np

sharpen = [0, -1, 0, -1, 5, -1, 0, -1, 0]
edgedetection1 = [1, 0, -1, 0, 0, 0, -1, 0, 1]
edgedetection2 = [0, 1, 0, 1, -4, 1, 0, 1, 0]
edgedetection3 = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
boxblur = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
gaussianblur = [1/16, 1/8, 1/16, 1/8, 1/4, 1/8, 1/16, 1/8, 1/16]
                
if __name__ == "__main__":
    im = Image.open("ressources/orig.png")
    im.show()
    listim = list(im.getdata())
    listr, listg, listb = zip(*listim)

    kernel = edgedetection3

    listr = [int(i) for i in convolution(listr, kernel)]
    listg = [int(i) for i in convolution(listg, kernel)]
    listb = [int(i) for i in convolution(listb, kernel)]

    listim = list(zip(listr, listg, listb))
    im2 = Image.new(im.mode, im.size)
    im2.putdata(listim)
    im2.show()
