#!/usr/bin/env python

from distutils.core import setup

setup(name='hellomenzi',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='menzi.mail@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
      executables = [Executable("hellomenzi.py")]
     )

