# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rvaconnect
version = rvaconnect.__version__

setup(
    name='rvaconnect',
    version=version,
    author='',
    author_email='ben@wellfire.co',
    packages=[
        'rvaconnect',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['rvaconnect/manage.py'],
)