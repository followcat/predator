import base64
from io import BytesIO

from PIL import Image
import pytesseract


def image_from_base64(data):
    im = Image.open(BytesIO(base64.b64decode(data)))
    return im


def preprocess(img):
    img = img.convert("RGBA")
    img = img.resize( (img.size[0]*4, img.size[1]*4), Image.BILINEAR )
    pixdata = img.load()

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0]*pixdata[x, y][1]*pixdata[x, y][2] > 6502500/1.5:
                pixdata[x, y] = (255, 255, 255, 255)
            else:
                pixdata[x, y] = (0, 0, 0, 255)
    return img


def image_to_string(img):
    return pytesseract.image_to_string(img)
