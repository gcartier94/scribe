"""
Scribe - CLI tool to manage to-do notes.

This program and the accompanying materials are made available under the terms of
The MIT License which accompanies this distribution, and is available at

https://mit-license.org/

SPDX-License-Identifier: MIT

Copyright (c) 2020 Guilherme Cartier.
"""

#!/usr/bin/env python


import os
import random
import datetime
import json
from clint.textui import colored, puts, columns
from cli import Cli

dir_path = os.path.dirname(os.path.realpath(__file__))

TODOS_DIRECTORY = 'notes'
TODOS_FILE = 'notes.json'

class Scribe:

    def __init__(self):

        self.cli = Cli()

    def start(self):
        pass


if __name__ == '__main__':
    scribe = Scribe()
    print(scribe.cli.args)
