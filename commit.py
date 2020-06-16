import os, sys
from utils import showStatus, clear, output, manualMode
from commit_utils import extraOptions, commonCmdLoop, resetMode, commitMode


# Start the command loop
def commit_tool():
  tool_on = True
  while tool_on:
    #Process arguments
    mode = input("""
Choose a mode:

(a)dd mode: Add files to staging
(d)iscard mode: Discard unstaged changes
(r)eset mode: Reset files from staging
(c)ommit mode: Commit staged changes

Extra:
Include ~ in front of your command to execute any command
(t) git status
(e)xit tool
(q)uit

:""")

    if mode == "e":
      clear()
      tool_on = False
    elif mode == "q":
      clear()
      sys.exit()
    elif mode == "t":
      clear()
      showStatus()
    elif mode == "a":
      commonCmdLoop(
        "Choose which files to stage",
        "git add",
        "M ",
        "M  "
      )
    elif mode == "d":
      commonCmdLoop(
        "Choose which files to stage",
        "git checkout",
        "M ",
        "M  "
      )
    elif mode == "r":
      resetMode()
    elif mode == "c":
      commitMode()
    elif mode == "l":
      # git log --pretty=oneline
      print('something')
    else:
      manualMode(mode)