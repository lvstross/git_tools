import os, sys
from utils import showStatus, clear, output, manualMode, extraOptions

# Utils

# Show Stash
def showStash():
  print("*** Stash List ***")
  os.system("git stash list")

def commonCmdLoop(opMsg, systemCmd):
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    print("")
    showStash()
    index = input("""

Index: """)
    manualMode(index)
    if index == "t":
      showStatus()
    else:
      os.system(systemCmd + " stash@{" + index + "}")
  clear()