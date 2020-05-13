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
        self.todo_json = self.load_todos()
        self.todo_list = self.todo_json['todo_list']
        self.number_of_todos = len(self.todo_list)

    def load_todos(self):
        with open(os.path.join(dir_path, TODOS_DIRECTORY, TODOS_FILE), 'r') as json_file:
            return json.load(json_file)

    def start(self):
        if self.cli.args.add:
            json_todo = self.build_todo(self.cli.args.add)
            self.todo_list.append(json_todo)
            save_json = {"todo_list": self.todo_list}
            self.save_todos(save_json)
            if not self.cli.args.silent:
                self.list_todos()
        if self.cli.args.update:
            self.update_todo_description(self.cli.args.update[0], self.cli.args.update[1])
            if not self.cli.args.silent:
                self.list_todos()
        if self.cli.args.delete:
            self.delete_todo(self.cli.args.delete)
            if not self.cli.args.silent:
                self.list_todos()            
        if self.cli.args.list:
            self.list_todos()
        if self.cli.args.check:
            self.change_todo_status(self.cli.args.check, 'completed')
            if not self.cli.args.silent:
                self.list_todos()
        if self.cli.args.wip:
            self.change_todo_status(self.cli.args.wip, 'wip')
            if not self.cli.args.silent:
                self.list_todos()            
        if self.cli.args.revert:
            self.change_todo_status(self.cli.args.revert, 'waiting')
            if not self.cli.args.silent:
                self.list_todos()            
        if self.cli.args.incomplete:
            self.change_todo_status(self.cli.args.incomplete, 'incomplete')
            if not self.cli.args.silent:
                self.list_todos()            

    def delete_todo(self, todo_id):
        for i in range(len(self.todo_list)):
            if self.todo_list[i]['todo_id'] == todo_id:
                self.todo_list.pop(i)
                save_json = {"todo_list": self.todo_list}
                self.save_todos(save_json)
                break


    def build_todo(self, todo_description):
        hash_id = random.getrandbits(16)
        #increment = str(self.number_of_todos + 1)
        today = datetime.datetime.today()
        today_str = today.strftime('%m/%d/%Y @ %H:%M:%S')
        return {
            'todo_id': str('%0x' % hash_id),
            'todo_description': todo_description,
            'status': 'waiting',
            'created_on': today_str
        }         
   
    def save_todos(self, save_json):
        with open(os.path.join(dir_path, TODOS_DIRECTORY, TODOS_FILE), 'w') as json_file:
            json.dump(save_json, json_file)
        
    def list_todos(self):
        puts(f"{columns([('ID'), 5],[('Status'), 8], [('Description'), 60], [('Created on'), 20])}")
        puts("-"*100)
        for todo in self.todo_list:
            status = ''
            if todo['status'] == 'completed':
                status = colored.green('C')
            elif todo['status'] == 'wip':
                status = colored.magenta('W')
            elif todo['status'] == 'waiting':
                status = colored.blue('+')
            elif todo['status'] == 'incomplete':
                status = colored.red('X')                
            puts(f"[ {todo['todo_id']} ] [ {status} ] > {columns([(todo['todo_description']), 60]) } {'|'} <{todo['created_on']}>")
    
    def change_todo_status(self, todo_id, status):
        for todo in self.todo_list:
            if todo['todo_id'] == todo_id:
                todo['status'] = status
                save_json = {"todo_list": self.todo_list}
                self.save_todos(save_json)
    
    def update_todo_description(self, todo_id, updated_description):
        for todo in self.todo_list:
            if todo['todo_id'] == todo_id:
                todo['todo_description'] = updated_description
                save_json = {"todo_list": self.todo_list}
                self.save_todos(save_json)

if __name__ == '__main__':
    cli = Cli()
    scribe = Scribe()
    scribe.start()
