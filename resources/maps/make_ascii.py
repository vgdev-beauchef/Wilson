import numpy as np
import cv2

def compare(array,(a,b,c)):
    return array[0]==c and array[1]==b and array[2]==a

def main(infile,outfile):
    image = cv2.imread(infile,cv2.CV_LOAD_IMAGE_COLOR)
    (w,h,c) = image.shape
    a=open(outfile,'w')
    for y in xrange(h):
        for x in xrange(w):
            if compare(image[x,y],(255,216,0)): a.write(".")
            elif compare(image[x,y],(127,201,255)): a.write("-")
            elif compare(image[x,y],(0,38,255)): a.write("~")
            elif compare(image[x,y],(0,255,144)): a.write("/")
            elif compare(image[x,y],(127,0,0)): a.write("#")
            elif compare(image[x,y],(0,0,0)): a.write("O")
        a.write("\n")
    a.close()

if __name__ == '__main__':
    import sys
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    main(name1,name2)
