#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Mario S. Könz <mskoenz@gmx.net>

import sys
import click
import subprocess
__all__ = ["full_cppcheck"]

@click.command()
@click.argument('src', nargs=-1)
def full_cppcheck(src):
    if not src:
        return
    cmd = ("cppcheck","--quiet", "--enable=missingInclude,portability,performance,style,warning", "--std=c++14") + src
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode or res:
        print(res.stdout.decode("utf-8").strip())
        sys.exit(1)
