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

```python
from colorspaces import create_image_by_lab, show_image

image = create_image_by_lab(lightness=53, a=80, b=67)
show_image(image, title="A red image")
```
