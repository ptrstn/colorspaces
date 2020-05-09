from setuptools import setup

setup(
    name="colorspaces",
    version="0.0.1",
    url="http://github.com/ptrstn/colorspaces",
    author="Peter Stein",
    license="WTFPL",
    packages=["colorspaces"],
    install_requires=["numpy", "matplotlib", "Pillow", "scikit-image"],
)
