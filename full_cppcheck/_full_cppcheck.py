#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Mario S. Könz <mskoenz@gmx.net>

import sys
import click


@click.command
def full_cppcheck():
    print("bla")
    click.exit(1)
