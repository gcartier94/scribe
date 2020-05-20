"""
Scribe - CLI tool to manage to-do notes.

This program and the accompanying materials are made available under the terms of
The MIT License which accompanies this distribution, and is available at

https://mit-license.org/

SPDX-License-Identifier: MIT

Copyright (c) 2020 Guilherme Cartier.
"""

from clint.textui import puts, colored, columns


class Display():
    """
    Class responsible for anything related to displaying notes in a pretty way
    """
    def __init__(self):
        pass

    def list_notes(self, context_list):
        for context in context_list:
            if context['note_list']:
                puts(f"{colored.cyan(context['context'])}")
                puts("-"*100)
                puts(self.build_default_display_for_non_complete_status(context['note_list']))
                puts(self.build_default_display_for_complete_status(context['note_list']))

    def build_default_display_for_non_complete_status(self, note_list):
        display_str = ''
        for note in note_list:
            if note['status'] != 'completed':
                display_str += f"<{note['note_id']}>. "
                display_str += f"[ {self.define_status_string(note['status'])} ] - "
                display_str += f"{columns([(note['short_description']), 40])} |\n"
        return display_str

    def build_default_display_for_complete_status(self, note_list):
        display_str = ''
        for note in note_list:
            if note['status'] == 'completed':
                display_str += f"<{note['note_id']}>. "
                display_str += f"[ {colored.green('X', bold=True)} ] - "
                display_str += f"{columns([(note['short_description']), 40])} | "
                display_str += f"{colored.green(note['completed_on'])} \n"
        return display_str

    def lont_list_notes(self):
        print('long list')

    def define_status_string(self, status):
        if status == 'wip':
            return colored.magenta('W', bold=True)
        if status == 'waiting':
            return colored.blue('+', bold=True)
