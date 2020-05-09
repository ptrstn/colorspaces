[![Build Status](https://travis-ci.com/ptrstn/colorspaces.svg?branch=master)](https://travis-ci.com/ptrstn/colorspaces)
[![codecov](https://codecov.io/gh/ptrstn/colorspaces/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/colorspaces)

# colorspaces

A repository to play around with color spaces, especially L\*a\*b\*, using ```Pillow``` and ```scikit-image```.

## Installation

```bash
pip install git+https://github.com/ptrstn/colorspaces
```

## Usage

### Example 

#### L\*a\*b\* <-> RGB conversion

```python
import numpy
from colorspaces import convert_lab_array_to_rgb, convert_rgb_array_to_lab

rgb_array = numpy.array([[[255, 0, 0]]], dtype="uint8")
lab_array = convert_rgb_array_to_lab(rgb_array)
rgb_array = convert_lab_array_to_rgb(lab_array)

print(lab_array)
print(rgb_array)
```

```
[[[53.24058794 80.09230823 67.20275104]]]
[[[255   0   0]]]
```

#### Create RGB image by  L\*a\*b\* values

```python
from colorspaces import create_image_by_lab, show_image

image = create_image_by_lab(lightness=53, a=80, b=67)
show_image(image, title="A red image")
```
