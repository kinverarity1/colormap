# Use the setuptools package if it is available. It's preferred 
# because it creates an exe file on Windows for Python scripts.

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from distutils.core import setup


setup(name='newcolormaps',
      packages=["newcolormaps", ],
      )
