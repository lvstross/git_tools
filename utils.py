import os

extraOptions = "(b)-back | (~)-execute any command, (t)-git status"

def showStatus():
  os.system("git status")

def showBranch():
  os.system("git branch")

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