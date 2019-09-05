import subprocess
import os
import argparse
import sys

dbstore_directory = os.path.expanduser('~/.tl')
dbfile_directory = os.path.expanduser('~/.tl/db')

if not os.path.exists(dbfile_directory):
    try:
      os.makedirs(dbstore_directory)
    except:
      pass
    with open(dbfile_directory, 'w+') as listdb:
      pass

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-a", "--add", help="Add an item.")
    parser.add_argument("-g", "--get", help="Get the list.")
    parser.add_argument("-c", "--clean", help="Clean the list.")
    options = parser.parse_args(args)
    return options

options = getOptions(sys.argv[1:])

def get():
  todolist = 'Your List:\n'
  with open(dbfile_directory, 'r') as listdb:
    todolist += "\n".join(listdb.readlines())
  subprocess.Popen(['notify-send', todolist])

def add(message):
  with open(dbfile_directory, 'a') as listdb:
    listdb.write('# '+message+"\n")

if options.add:
  add(options.add)
elif options.get:
  get()
elif options.clean:
  pass