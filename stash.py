import os, sys
from utils import showStatus, clear, output, manualMode
from stash_utils import extraOptions, commonCmdLoop


# Start the command loop
def stash_tool():
  tool_on = True
  while tool_on:
    # Process arguments
    mode = input("""
Choose a mode:

(s)ave mode: Save a stash
(a)pply mode: Apply a stash
(v)iew mode: View a stash
(d)rop mode: Drop a stash

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
    elif mode == "s":
      clear()
      stashMode = input("""
  Choose a stash option:

  (d)efault: Stash all changes as last commit message
  (m)essage: Stash all changes with your own stash message
  (p)ick: Stash changes in groups with your own stash message
  (b)ack: <-
  """)

      if stashMode == "d":
        os.system("git stash")
      elif stashMode == "m":
        msg = input("Enter a stash message: ")
        os.system("git stash save " + msg)
      elif stashMode == "p":
        msg = input("Enter a stash message: ")
        os.system("git stash save -p " + msg)

    elif mode == "a":
      commonCmdLoop(
        "Choose an index to apply",
        "git stash apply"
      )
    elif mode == "v":
      commonCmdLoop(
        "Choose an index to view the stash diff",
        "git stash show -p"
      )
    elif mode == "d":
      commonCmdLoop(
        "Choose an index to drop a stash",
        "git stash drop"
      )
    else:
      manualMode(mode)
