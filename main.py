#!/usr/bin/python3
import sys
from utils import clear, output, manualMode
from stash import stash_tool
from branch import branch_tool
from commit import commit_tool

# Check if current directory is a git repo
try:
  with open('./.git/HEAD') as f:
    clear()
except IOError:
  clear()
  print("This is not a git repository")
  sys.exit()


# Get initial starting point
while True:
  tool = input("""
Choose a tool:

(c)ommit tools
(b)ranch tools
(s)tash tools

Extra:
Include ~ in front of your command to execute any command
(q)uit

:""")
  if tool == 'c':
    clear()
    commit_tool()
  elif tool == 'b':
    clear()
    branch_tool()
  elif tool == 's':
    clear()
    stash_tool()
  elif tool == 'q':
    sys.exit()
  else:
    manualMode(tool)