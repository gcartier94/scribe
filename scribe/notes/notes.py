import os
import json
import random
import datetime

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
NOTES_DIRECTORY = os.path.join(CURRENT_DIR, 'data')
NOTES_FILE = os.path.join(NOTES_DIRECTORY, 'data.json')


class Notes:

    def __init__(self):
        self.notes_json = self.load_notes()
        self.note_list = self.notes_json['note_list']
        self.context_list = ['Misc']
        self.load_context_list()
        self.number_of_notes = len(self.note_list)

    def load_notes(self):
        with open(NOTES_FILE, 'r') as json_file:
            return json.load(json_file)

    def load_context_list(self):
        for note in self.note_list:
            context = note['context']
            if context not in self.context_list:
                self.context_list.append(context)

    def save_note(self):
        save_json = {"note_list": self.note_list}
        with open(NOTES_FILE, 'w') as json_file:
            json.dump(save_json, json_file)

    def generate_hash_id(self):
        bits = random.getrandbits(16)
        return str('%04x' % bits)

    def generate_note(self, short_description, context=None):
        hash_id = self.generate_hash_id()
        right_now = datetime.datetime.now()
        right_now_str = right_now.strftime('%m/%d/%Y @ %H:%M')
        note_json = {
            'note_id': hash_id,
            'context': context,
            'short_description': short_description,
            'status': 'waiting',
            'created_on': right_now_str,
            'deadline': None,
            'completed_on': None,
            'time_to_complete': None,
            'time_to_deadline': None,
            'priority': None,
            'detailed_description': None
        }
        self.note_list.append(note_json)
        self.save_note()

    def update_note_attribute(self, note_id, attribute, value):
        note = self.get_note_by_id(note_id)
        note[attribute] = value
        self.save_note()

    def get_note_by_id(self, note_id):
        for note in self.note_list:
            if note['note_id'] == note_id:
                return note

    def get_note_index_by_note_id(self, note_id):
        for i in range(len(self.note_list)):
            if self.note_list[i]['note_id'] == note_id:
                return i
        print('Unable to find note')
        exit(1)

    def delete_note(self, note_id):
        note_index = self.get_note_index_by_note_id(note_id)
        self.note_list.pop(note_index)
        self.save_note()

    def move_note(self, note_id, position):
        origin_position = ''
        target_position = ''
        for i in range(len(self.note_list)):
            note = self.note_list[i]
            if note['note_id'] == note_id:
                origin_position = i
            if i == int(position):
                target_position = i
        if str(origin_position) and str(target_position):
            temporary_storage = self.note_list[target_position]
            self.note_list[target_position] = self.note_list[origin_position]
            self.note_list[origin_position] = temporary_storage
            self.save_note()


