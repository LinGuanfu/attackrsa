#!/usr/bin/env python

from setuptools import *

setup(
    name = 'attackrsa',
    version = '0.1.1',
    install_requires = ['gmpy2'],
    packages = ['attackrsa'],
    scripts = ['bin/attackrsa']
)

    
