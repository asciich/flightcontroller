#!/usr/bin/env python

from distutils.core import setup

setup(name='amavlink',
      version='0.06',
      description='MAVLink communication library',
      author='Reto Hasler',
      author_email='reto.hasler@asciich.ch',
      url='https://github.com/asciich/flightcontroller',
      packages=['amavlink'],
      install_requires=['pymavlink'],
      entry_points={
          'console_scripts': ['amavlink=amavlink.AMavlinkCLI:main'],
      }
      )
