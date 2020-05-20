"""
Scribe - CLI tool to manage to-do notes.

This program and the accompanying materials are made available under the terms of
The MIT License which accompanies this distribution, and is available at

https://mit-license.org/

SPDX-License-Identifier: MIT

Copyright (c) 2020 Guilherme Cartier.
"""

import argparse
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from actions import (AddNote,
                     ListNotes,
                     DeleteNote,
                     CompleteNote,
                     WipNote,
                     UpdateNote,
                     LongListNotes,
                     RevertNote,
                     ListContext,
                     SetContext,
                     TestAction)

VERSION = '0.1.0'
PROGRAM_NAME = 'Scribe'


class Cli:
    """
    Class for the CLI based on argparse
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='scribe',
                                              usage='%(prog)s [options]',
                                              description='Manage notes and to-do\'s using a CLI',
                                              epilog='Have a great day! Now get things done!')

        self.parser.version = f'{PROGRAM_NAME} - {VERSION}'
        self.initialize_base_arguments()
        self.args = self.parser.parse_args()

    def initialize_base_arguments(self):

        self.parser.add_argument('-v',
                                 '--version',
                                 action='version',
                                 help='display program version')

        self.parser.add_argument('-s',
                                 '--silent',
                                 action='store_true',
                                 help='silent mode')

        self.parser.add_argument('list',
                                 nargs=0,
                                 action=ListNotes,
                                 help='normal list all to-do notes')

        self.parser.add_argument('-l',
                                 '--long',
                                 nargs=0,
                                 action=LongListNotes,
                                 help='long list all to-do notes')

        self.parser.add_argument('--context',
                                 action=ListContext,
                                 help='list context available and context set')

        self.parser.add_argument('--set-context',
                                 action=SetContext,
                                 help='set a new context')

        self.parser.add_argument('-a',
                                 '--add',
                                 metavar='NOTE',
                                 action=AddNote,
                                 type=str,
                                 help='add new to-do note')

        self.parser.add_argument('-d',
                                 '--delete',
                                 action=DeleteNote,
                                 metavar='TODO',
                                 help='delete to-do note')

        self.parser.add_argument('-u',
                                 '--update',
                                 nargs=2,
                                 metavar='TODO',
                                 action=UpdateNote,
                                 help='update a to-do description')

        self.parser.add_argument('-c',
                                 '--complete',
                                 action=CompleteNote,
                                 metavar='TODO',
                                 help='mark a to-do complete')

        self.parser.add_argument('-r',
                                 '--revert',
                                 action=RevertNote,
                                 metavar='TODO',
                                 help='revert a to-do to waiting status')

        self.parser.add_argument('-w',
                                 '--wip',
                                 action=WipNote,
                                 metavar='TODO',
                                 help='mark a to-do as in progress')
