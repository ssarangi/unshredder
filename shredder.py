from PIL import Image
from random import shuffle
import sys


def shred(img_file, output_file, num_shreds=10):
    image = Image.open(img_file)
    shredded = Image.new("RGBA", image.size)
    width, height = image.size
    shred_width = width // num_shreds
    sequence = range(0, num_shreds)
    shuffle(sequence)

    for i, shred_idx in enumerate(sequence):
        shred_x1, shred_y1 = shred_width * shred_idx, 0
        shred_x2, shred_y2 = shred_x1 + shred_width, height
        region = image.crop((shred_x1, shred_y1, shred_x2, shred_y2))
        shredded.paste(region, (shred_width * i, 0))

    shredded.save(output_file)

if __name__ == "__main__":
    args = len(sys.argv)
    if args < 2:
        print("Error: expected arguments -> shredder.py <inp_file> <out_file> <optional>num_shreds")

    inp_file = sys.argv[0]
    out_file = sys.argv[1]
    if args == 3:
        num_shreds = int(sys.argv[2])
        shred(inp_file, out_file, num_shreds)
    else:
        shred(inp_file, out_file)