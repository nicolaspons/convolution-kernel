from convolution import convolution
from PIL import Image
import sys

identity = [0, 0, 0, 0, 1, 0, 0, 0, 0]

def switch(x):
    switcher = {
        'sharpen' : [0, -1, 0, -1, 5, -1, 0, -1, 0],
        'edgedetection1' : [1, 0, -1, 0, 0, 0, -1, 0, 1],
        'edgedetection2' : [0, 1, 0, 1, -4, 1, 0, 1, 0],
        'edgedetection3' : [-1, -1, -1, -1, 8, -1, -1, -1, -1],
        'boxblur' : [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9],
        'gaussianblur' : [1/16, 1/8, 1/16, 1/8, 1/4, 1/8, 1/16, 1/8, 1/16]
    }
    return switcher.get(x, identity)

def main():
    if len(sys.argv) == 1:
        print("main.py: 2 args are needed\n\t$ python main.py 'imgsrc' 'kernel'")
        print("kernel available:\n\tsharpen\n\tedgedetection1\n\tedgedetection2\n\tedgdetection3\n\tboxblur\n\tgaussianblur")
        sys.exit(1)
    else:
        im = Image.open(sys.argv[1])
        im.show()
        listim = list(im.getdata())
        listr, listg, listb = zip(*listim)
        kernel = switch(sys.argv[2])
        listr = [int(i) for i in convolution(listr, kernel)]
        listg = [int(i) for i in convolution(listg, kernel)]
        listb = [int(i) for i in convolution(listb, kernel)]
        listim = list(zip(listr, listg, listb))
        im2 = Image.new(im.mode, im.size)
        im2.putdata(listim)
        im2.show()
        sys.exit(0)

if __name__ == "__main__":
    main()