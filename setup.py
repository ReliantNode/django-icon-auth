#!/usr/bin/env python

from setuptools import setup

setup(name='django-icon-auth',
      version='0.1',
      description='Icon authentication middleware for Django',
      url='https://github.com/ReliantNode/django-icon-auth',
      packages=['iconauth'],
      install_requires=['django>=1.10', 'iconservice>=1.6.0'],
     )