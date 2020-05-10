import math

import numpy
import pytest
from skimage.color import lab2xyz

from colorspaces import (
    create_image_by_rgb,
    create_image_by_lab,
    show_image,
    convert_rgb_array_to_lab,
    convert_lab_array_to_rgb,
)


def test_create_image_by_rgb():
    image = create_image_by_rgb(255, 0, 0)
    image_array = numpy.array(image)
    assert numpy.array_equal(image_array[0, 0, :], numpy.array([255, 0, 0]))


def test_create_image_by_lab():
    image = create_image_by_lab(53, 80, 67)
    image_array = numpy.array(image)
    assert numpy.array_equal(image_array[0, 0, :], numpy.array([254, 0, 0]))


def test_convert_rgb_array_to_lab():
    rgb_array = numpy.array([[[255, 0, 0]]], dtype="uint8")
    lab_array = convert_rgb_array_to_lab(rgb_array)
    expected_array = numpy.array([[[53.24058794, 80.09230823, 67.20275104]]])
    assert numpy.allclose(lab_array, expected_array)


def test_lab2xyz_user_warning():
    """
    Show how the xyz color space is not a complete superset of all possible L*a*b combinations.
    z should always be greater than zero but are not in this example.

    See: https://github.com/scikit-image/scikit-image/issues/4506
    """
    with pytest.warns(UserWarning):
        xyz_array = lab2xyz(numpy.array([[[0, -13.70470524, 27.88690567]]]))

    x, y, z = xyz_array[0, 0, :]

    expected_x = -0.00334555
    expected_y = 0
    expected_z = -0.01928643

    assert math.isclose(x, expected_x, rel_tol=1e-06)
    assert math.isclose(y, expected_y)
    assert math.isclose(z, expected_z, rel_tol=1e-06)


def test_convert_lab_array_to_rgb():
    lab_array = numpy.array([[[53.24058794, 80.09230823, 67.20275104]]])
    rgb_array = convert_lab_array_to_rgb(lab_array)
    expected_array = numpy.array([[[255, 0, 0]]], dtype="uint8")
    assert numpy.allclose(rgb_array, expected_array)


def test_show_image():
    image = create_image_by_lab(53, 80, 67)
    show_image(image, title="Red image in RGB created by L*a*b* values")
