import sys
import os
from argparse import Action
from clint.textui import puts, colored, columns

sys.path.insert(0, os.path.abspath('..'))

from notes import Notes


note_manager = Notes()

class TestAction(Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(TestAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(f'These are the values: {values}')
        setattr(namespace, self.dest, values)

class ListNotes(Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(ListNotes, self).__init__(option_strings=option_strings, dest=dest,
                                        nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if not namespace.silent and not namespace.long:
            puts('Normal list')
            puts('-'*100)
            for i in range(len(note_manager.note_list)):
                note = note_manager.note_list[i]
                puts(f"{str(i).rjust(4)}. <{note['note_id']}> [ {note['status']} ] -"
                     f"{note['short_description']}| "
                     f"{colored.cyan('P')} |"
                     )

class LongListNotes(Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(LongListNotes, self).__init__(option_strings=option_strings, dest=dest,
                                        nargs=0, required=False, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        puts('Long list')
        puts('-'*140)
        for i in range(len(note_manager.note_list)):
            note = note_manager.note_list[i]
            index_str = str(i).rjust(4)
            note_id = note['note_id']
            status = self.define_status_string(note['status'])
            short_description = note['short_description']
            created_on = note['created_on']
            deadline = note['deadline']
            div = [('|'), 1]
            puts(f"{index_str}. <{note_id}> [ {status} ] - "
                 f"{columns([(short_description), 50])}|"
                 f"{colored.cyan('P')} |"
                 f"{colored.blue('C')} {created_on} |"
                 f"{colored.red('D')} {deadline} |"
                 f"{colored.magenta('T')} |")
        setattr(namespace, self.dest, True)

    def define_status_string(self, status):
        if status == 'completed':
            return colored.green('X', bold=True)
        if status == 'wip':
            return colored.magenta('W', bold=True)
        if status == 'waiting':
            return colored.blue('+', bold=True)

class AddNote(Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(AddNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.generate_note(values, context=namespace.context)

class DeleteNote(Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(DeleteNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.delete_note(values)

class CompleteNote(Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(CompleteNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values, 'status', 'completed')

class WipNote(Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(WipNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values, 'status', 'wip')

class RevertNote(Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super(RevertNote, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values, 'status', 'waiting')

class UpdateNote(Action):
    def __init__(self, option_strings, dest, nargs=2, **kwargs):
        super(UpdateNote, self).__init__(option_strings, dest, nargs=2, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.update_note_attribute(values[0], 'short_description', values[1])

class MoveNote(Action):
    def __init__(self, option_strings, dest, nargs=2, **kwargs):
        super(MoveNote, self).__init__(option_strings, dest, nargs=2, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        note_manager.move_note(values[0], values[1])