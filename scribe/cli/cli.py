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
                                              description='Manage notes and to-do\'s using a CLI',
                                              epilog='Have a great day! Now get things done!')
        self.parser.version = f'{PROGRAM_NAME} - {VERSION}'
        self.initiate_arguments()
        self.args = self.parser.parse_args()
   
    def initiate_arguments(self):

        self.parser.add_argument('-v',
                                 '--version',
                                 action='version',
                                 help='display program version')

        self.parser.add_argument('-s',
                                 '--silent',
                                 action='store_true',
                                 help='silent mode')

        self.parser.add_argument('-l',
                                 '--list',
                                 action='store_true',
                                 help='list all to-do notes')

        self.parser.add_argument('-a',
                                 '--add',
                                 metavar='NOTE',
                                 type=str,
                                 help='add new to-do note')

        self.parser.add_argument('-d',
                                 '--delete',
                                 metavar='TODO',
                                 help='delete to-do note')

        self.parser.add_argument('-u',
                                 '--update',
                                 nargs=2,
                                 metavar='TODO',
                                 help='update a to-do description')                                 

        self.parser.add_argument('-c',
                                 '--check',
                                 metavar='TODO',
                                 help='mark a to-do complete')
    
        self.parser.add_argument('-r',
                                 '--revert',
                                 metavar='TODO',
                                 help='revert a to-do to waiting status')
        
        self.parser.add_argument('-w',
                                 '--wip',
                                 metavar='TODO',
                                 help='mark a to-do as in progress')        
     
        self.parser.add_argument('-i',
                                 '--incomplete',
                                 metavar='TODO',
                                 help='mark a to-do incomplete')