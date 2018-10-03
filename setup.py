#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Mario S. Könz <mskoenz@gmx.net>

from setuptools import setup

setup(
    name='cppcheck_hook',
    description='Wrapper for cppcheck',
    url='https://github.com/mskoenz/pre-commit-cppcheck',
    version='0.1.0',
    author='Mario S. Könz',
    author_email='mskoenz@gmx.net',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['cppcheck_hook'],
    install_requires=['click'],
    entry_points="""
        [console_scripts]
        cppcheck_hook=cppcheck_hook:cppcheck_hook
        """,
)
