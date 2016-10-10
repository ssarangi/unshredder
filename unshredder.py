from PIL import Image
import sys

class UnshreddedImage:
    def __init__(self, img):
        self.img = img

    @property
    def size(self):
        return self.img.size

    def get_pixel(self, x, y):
        data = self.img.getdata()
        width, height = self.img.size
        pixel = data[y * width + x]
        return pixel

    def get_column_pixels(self, column):
        pixels = []
        width, height = self.img.size
        if column < width:
            for y in range(0, height):
                pixels.append(self.get_pixel(column, y))

        return pixels

    def save(self, filename):
        self.img.save(filename, "PNG")

class Unshredder:
    def __init__(self, unshredded_img, num_shreds):
        self.original = Image.open(unshredded_img)
        self.regions = []
        self.num_shreds = num_shreds
        width, height = self.original.size

        for i in range(0, num_shreds):
            box = (i * width // num_shreds, 0, (i+1) * width // num_shreds, height)
            region = UnshreddedImage(self.original.crop(box))
            self.regions.append(region)

    def save_regions(self):
        for idx, i in enumerate(self.regions):
            i.save(str(idx) + ".png")

def read_img(filename):
    im = Image.open(filename)
    return im


def main():
    filename = sys.argv[1]
    unshredder = Unshredder(filename, 20)

if __name__ == "__main__":
    main()
