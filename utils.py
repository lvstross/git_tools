import os
import subprocess

extraOptions = "(b)-back | (~)-execute any command, (t)-git status"

def cli(cmd):
  result = subprocess.run(cmd, stdout=subprocess.PIPE)
  result.stdout

def showStatus():
  cli(['git', 'status'])


def showBranch():
  cli(['git', 'branch'])

def clear():
  os.system("clear")

def output(o):
  print("Output: {}".format(o))

# this should turn into something that allows many extra commands
# and searches for various possible argutments to show status, branchs
# or other quick command line options like pwd, ls -la and so on. Even provide
# a help argument to show all extra commands
def manualMode(arg):
  if "~" in arg:
    clear()
    os.system(arg[1:])