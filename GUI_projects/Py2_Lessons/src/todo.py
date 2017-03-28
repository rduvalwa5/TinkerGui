#!/usr/local/bin/python3
'''
Created on Mar 8, 2013

@author: rduvalwa2
todo.py  '''

import sys

otask = open('open_tasks.txt', 'a')  # opens and creates file
otask.close()
dtask = open('done_tasks.txt', 'a')
dtask.close()
options = ('add', 'done', 'quit')
string_input = 'Pick an option from the list (%s): ' % ','.join(options)  # saves on typing the same string
while True:
    open_tasks = open('open_tasks.txt', 'r').readlines()  # open and read from same expression
# open and print open tasks
    if open_tasks:
            print('-' * 10)  # print 10 -
            print('Open Tasks')
            print('-' * 10) 
            for i, task in enumerate(open_tasks):
                print(i, task.strip())  # remove leding and lagging spaces
# open and print done tasls
    done_tasks = open('done_tasks.txt', 'r').readlines()
    print('-' * 12)
    print('Done Tasks')
    print('-' * 12)
    for i, task in enumerate(done_tasks):
        print(i, task.strip())
# start case statment        
    inp = input(string_input)  # see saves typing
    if inp not in options:  # by creating options the input can be tested against that list
        print('Please pick a valid option')
        continue  # keep loop running
    if inp == 'add':
        new_task = input('Enter new task" ')
        tasks = open('open_tasks.txt', 'a')  # append mode to add to file and not overwrite it
        tasks.write(new_task + '\n')
        tasks.close()
    if inp == 'done':
        while True:  # infinite loop
            done_task = input('Please enter the number of your completed task: ').strip()
            if done_task.isdigit():
                done_task = int(done_task)  # cast string to an int
                break
print('Please enter a task number')
open_tasks = open('open_tasks.txt', 'r').readlines()
for i, task in enumerate(open_tasks):
    if i == done_task:
        print('Task removed: {0}'.format(task))
        open_tasks.remove(task)
        f = open('open_tasks.txt', 'w')
        f.writelines(open_tasks)  # overwrite old file with new content
        f.close()
        f = open('done_tasks.txt', 'a')  # not overwriting done tasks just adding to it
        f.write(task)
        f.close()
#        break
                   
    if inp == 'quit':
        break  
# terminate the while loop
