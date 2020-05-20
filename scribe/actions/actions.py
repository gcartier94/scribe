"""
Scribe - CLI tool to manage to-do notes.

This program and the accompanying materials are made available under the terms of
The MIT License which accompanies this distribution, and is available at

https://mit-license.org/

SPDX-License-Identifier: MIT

Copyright (c) 2020 Guilherme Cartier.
"""

import sys
import os
import datetime
from argparse import Action
from utilities import Display
sys.path.insert(0, os.path.abspath('..'))

from notes import Notes


note_manager = Notes()
display = Display()


class TestAction(Action):
    """
    A simple test command
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(TestAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(f'These are the values: {values}')
        setattr(namespace, self.dest, values)


class ListNotes(Action):
    """
    Class for the regular/normal listing of notes
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(ListNotes, self).__init__(option_strings=option_strings, dest=dest,
                                        nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if not namespace.silent and not namespace.long and not namespace.context:
            return_list = []
            for context in note_manager.context_list:
                note_list = note_manager.get_note_list_by_context(context)
                return_list.append({'context': context, 'note_list': note_list})
            display.list_notes(return_list)


class LongListNotes(Action):
    """
    Class for the long listing of notes (not implemented)
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(LongListNotes, self).__init__(option_strings=option_strings, dest=dest,
                                            nargs=0, required=False, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        display.lont_list_notes()
        setattr(namespace, self.dest, True)


class AddNote(Action):
    """
    Class for adding a new note
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(AddNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.generate_note(values)


class DeleteNote(Action):
    """
    Class for deleting an existing note by note_id
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(DeleteNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.delete_note(values)


class CompleteNote(Action):
    """
    Class for marking an existing note complete by note_id
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(CompleteNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        completed_on = datetime.datetime.now()
        completed_on_str = completed_on.strftime('%m/%d/%Y @ %H:%M')
        note_manager.update_note_attribute(values, 'status', 'completed')
        note_manager.update_note_attribute(values, 'completed_on', completed_on_str)


class WipNote(Action):
    """
    Class for marking an existing note in progress by note_id
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(WipNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values, 'status', 'wip')


class RevertNote(Action):
    """
    Class for reverting the status of an existing note to 'waiting'
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(RevertNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values, 'status', 'waiting')


class UpdateNote(Action):
    """
    Class for updating the description of an existing note by note_id
    """
    def __init__(self, option_strings, dest, nargs=2, **kwargs):
        super(UpdateNote, self).__init__(option_strings, dest, nargs=2, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values[0], 'short_description', values[1])


class ListContext(Action):
    """
    Class for listing the available contexts and the active context
    """
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        super(ListContext, self).__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        for context in note_manager.context_list:
            if context in note_manager.current_context:
                print(f"|=> {context}")
            else:
                print(f"| {context}")
        setattr(namespace, self.dest, True)


class SetContext(Action):
    """
    Class for setting the context
    """
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(SetContext, self).__init__(option_strings, dest, nargs=1, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.current_context = values[0]
        note_manager.save_current_context()
        print(f'Context set to {values[0]}')
        setattr(namespace, 'context', True)
