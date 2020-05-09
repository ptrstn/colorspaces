import numpy

from colorspaces import create_image_by_rgb, create_image_by_lab
from colorspaces.core import show_image


def test_create_image_by_rgb():
    image = create_image_by_rgb(255, 0, 0)
    image_array = numpy.array(image)
    assert numpy.array_equal(image_array[0, 0, :], numpy.array([255, 0, 0]))


def test_create_image_by_lab():
    image = create_image_by_lab(53, 80, 67)
    image_array = numpy.array(image)
    assert numpy.array_equal(image_array[0, 0, :], numpy.array([254, 0, 0]))


def test_show_image():
    image = create_image_by_lab(53, 80, 67)
    show_image(image, title="Red image in RGB created by L*a*b* values")
