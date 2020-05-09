import numpy
import skimage
from PIL import Image
from matplotlib import pyplot
from skimage.color import lab2rgb


def create_image_by_lab(lightness, a, b):
    """
    Create a 500x500 RGB image by L*a*b* or CIELAB color space values

    :param lightness: L* indicates lightness with 0 as black and 100 as white
    :param a: a* color value where -128 is green and +128 is red
    :param b: b* color value where -128 is blue and +128 is yellow
    :return: Image
    """
    image = numpy.zeros((500, 500, 3))
    image[:, :, 0] = lightness
    image[:, :, 1] = a
    image[:, :, 2] = b

    image_rgb_float = lab2rgb(image)
    image_rgb_uint8 = skimage.img_as_ubyte(image_rgb_float)

    return Image.fromarray(image_rgb_uint8, mode="RGB")


def create_image_by_rgb(red, green, blue):
    rgb_pixel = numpy.zeros((500, 500, 3), dtype=numpy.uint8)
    rgb_pixel[:, :, 0] = red
    rgb_pixel[:, :, 1] = green
    rgb_pixel[:, :, 2] = blue
    return Image.fromarray(rgb_pixel, mode="RGB")


def show_image(image, title=None):
    pyplot.imshow(image)
    pyplot.axis("off")
    if title:
        pyplot.title(title)
    pyplot.show()
