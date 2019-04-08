#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


package_name = 'printhello'
filename = package_name + '.py'

setup(
    name=package_name,
    description='test python snap',
    py_modules=[package_name],
        entry_points={
        'console_scripts': [
            'printhello = printhello:main'
        ]
    },
)
