#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Mario S. Könz <mskoenz@gmx.net>
# pylint: disable=missing-docstring

import sys
import subprocess

import click
__all__ = ['cppcheck_hook']


@click.command()
@click.argument('src', nargs=-1)
def cppcheck_hook(src):
    if not src:
        return

    cmd = ('cppcheck', '--quiet', '--enable=all', '--std=c++14') + src

    res = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
    )
    err = res.stderr.strip().split('\n')

    actual_err = []
    for line in err:
        if line.startswith('(information)'):
            continue
        if '(style) The function' in line and 'is never used.' in line:
            continue
        if '(style) struct member' in line and 'is never used.' in line:
            continue
        actual_err.append(line)

    if res.returncode or actual_err:
        print('\n'.join(actual_err))
        sys.exit(1)
