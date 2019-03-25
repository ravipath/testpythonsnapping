#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


package_name = 'printhello'
filename = package_name + '.py'


def get_version():
    import ast

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


def get_long_description():
    try:
        with open('readme.txt', 'r') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name=ttpy,
    version=get_version(),
    author='reorx',
    author_email='ravipathak.de@gmail.com',
    description='test python snap',
    url='https://github.com/ravipath/testpythonsnapping.git',
    long_description=get_long_description(),
    py_modules=[package_name],
    license='License :: OSI Approved :: MIT License',
)
