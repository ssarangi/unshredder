from PIL import Image
import sys


def read_img(filename):
    im = Image.open(filename)
    return im


def main():
    filename = sys.argv[1]
    

if __name__ == "__main__":
    main()
