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
@click.option('--enable', default='all')
@click.option('--std', default='c++14')
def cppcheck_hook(enable, std, src):
    if not src:
        return

    print(enable, std)
    cmd = (
        'cppcheck', '--quiet', '--enable={}'.format(enable),
        '--std={}'.format(std)
    ) + src

    res = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
    )
    err = res.stderr.strip().split('\n')

    actual_err = []
    for line in err:
        if line == '':
            continue
        if line.startswith('(information)'):
            continue
        if '(style) The function' in line and 'is never used.' in line:
            continue
        if '(style) struct member' in line and 'is never used.' in line:
            continue
        actual_err.append(line)

    if actual_err:
        print('\n'.join(actual_err))
        sys.exit(1)
    if res.returncode:
        print(res.stdout.strip())
        sys.exit(res.returncode)
