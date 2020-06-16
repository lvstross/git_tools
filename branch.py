import os, sys
from utils import showStatus, clear, output, manualMode
from branch_utils import extraOptions, stepOptions, types, getIndexedBranches, commonCmdLoop, createNewBranch


# Start the command loop
def branch_tool():
  tool_on = True
  while tool_on:
    # Process arguments
    mode = input("""
Choose a mode:

(ck)eckout mode: Checkout a branch
(n)ew branch mode: Create a new branch
(d)elete mode: Delete a branch

Extras:
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
    elif mode == "ck":
      commonCmdLoop(
        "Choose a branch to checkout",
        "git checkout"
      )
    elif mode == "n":
      createNewBranch()
    elif mode == "d":
      commonCmdLoop(
        "Choose a branch to delete",
        "git branch -D"
      )
    else:
      manualMode(mode)
