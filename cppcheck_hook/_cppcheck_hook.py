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

    cmd = (
        'cppcheck',
        '--template=[{file}:{line}:{column}]: ({id}) {message}\n{code}',
        '--quiet',
        '--enable={}'.format(enable),
        '--std={}'.format(std),
    ) + src

    res = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
    )
    err = res.stderr.strip().split('\n')

    actual_err = []
    i = 0
    while i < len(err):
        line = err[i]
        errid = line.split('(', 1)[1].split(')', 1)[0]
        if line.startswith('[nofile'):
            code = None
            i += 1
            continue
        else:
            code = err[i + 1]
            highlight = err[i + 2]
            i += 3

            if 'cppcheck-disable={}'.format(errid) in code:
                continue

        if line == '':
            continue
        if 'The function' in line and 'is never used.' in line:
            continue
        if 'struct member' in line and 'is never used.' in line:
            continue
        actual_err.append(line)
        if code is not None:
            actual_err.append(code)
            actual_err.append(highlight)

    # print(actual_err)

    if actual_err:
        print('\n'.join(actual_err))
        sys.exit(1)
    if res.returncode:
        print(res.stdout.strip())
        sys.exit(res.returncode)
