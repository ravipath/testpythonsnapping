#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


package_name = 'printhello'
filename = package_name + '.py'

setup(
    name=package_name,
    #version=get_version(),
    #author='ravi',
    #author_email='ravipathak.de@gmail.com',
    description='test python snap',
    #url='https://github.com/ravipath/testpythonsnapping.git',
    scripts=['printhello.py']
    #long_description=get_long_description(),
    #py_modules=[package_name],
    #license='License :: OSI Approved :: MIT License',
)
