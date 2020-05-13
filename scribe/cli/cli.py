"""
Scribe - CLI tool to manage to-do notes.

This program and the accompanying materials are made available under the terms of
The MIT License which accompanies this distribution, and is available at

https://mit-license.org/

SPDX-License-Identifier: MIT

Copyright (c) 2020 Guilherme Cartier.
"""

import argparse

VERSION = '0.1.0'
PROGRAM_NAME = 'Scribe'

class Cli:

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='scribe',
                                              usage='%(prog)s [options]',
                                              description='Manage notes and to-do\'s using a CLI')
        self.parser.version = f'{PROGRAM_NAME} - {VERSION}'
        self.initiate_arguments()
        self.args = self.parser.parse_args()
    
    def initiate_arguments(self):

        self.parser.add_argument('-v',
                                 '--version',
                                 action='version',
                                 help='display program version')

        self.parser.add_argument('-l',
                                 '--list',
                                 help='list all to-do notes')
        