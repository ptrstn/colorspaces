import numpy


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


def test_convert_lab_array_to_rgb():
    rgb_array = numpy.array([[[255, 0, 0]]], dtype="uint8")
    lab_array = convert_rgb_array_to_lab(rgb_array)
    expected_array = numpy.array([[[53.24058794, 80.09230823, 67.20275104]]])
    assert numpy.allclose(lab_array, expected_array)


def test_convert_rgb_array_to_lab():
    lab_array = numpy.array([[[53.24058794, 80.09230823, 67.20275104]]])
    rgb_array = convert_lab_array_to_rgb(lab_array)
    expected_array = numpy.array([[[255, 0, 0]]], dtype="uint8")
    assert numpy.allclose(rgb_array, expected_array)


def test_show_image():
    image = create_image_by_lab(53, 80, 67)
    show_image(image, title="Red image in RGB created by L*a*b* values")
