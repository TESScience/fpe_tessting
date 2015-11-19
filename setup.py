#!/usr/bin/env python

from distutils.core import setup

setup(name='fpe_tessting',
      version='0.0.4',
      description='A test suite for the TESS FPE',
      author='Ed Bokhour',
      author_email='edbok@me.com',
      scripts=['bin/load_wrapper.py'],
      install_requires=['tessfpe']
     )
