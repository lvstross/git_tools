import os
from utils import showStatus, clear, output, manualMode, extraOptions

# Utils

# Common Command Loop
def commonCmdLoop(opMsg, systemCmd, contained, excluded):
  # @Note: 
  # Need to account for other status options (M, A, D, R, C, U)
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    files = os.popen("git status -s").read()
    splitFiles = files.split("\n")
    options = ""
    for i, file in enumerate(splitFiles):
      if contained in file and excluded not in file:
        options += "[{}]: {}\n".format(i, file)

    print(options)
    index = input("""

Index: """)
    if index == "t":
      showStatus()
    else:
      if index.isdigit():
        choosenFile = splitFiles[int(index)]
        print(systemCmd + " " + choosenFile[len(contained) + 1:])
        os.system(systemCmd + " " + choosenFile[len(contained) + 1:])
      else:
        output("Index must be an integer!")
    manualMode(index)

# Reset Mode
def resetMode():
  clear()
  index = ""
  while index != "b":
    output("Choose which files to unstage" + " or " + extraOptions)
    files = os.popen("git status -s").read()
    splitFiles = files.split("\n")
    options = ""
    for i, file in enumerate(splitFiles):
      if "M  " in file:
        options += "[{}]: {}\n".format(i, file)

    print(options)
    index = input("""

Index: """)
    if index == "t":
      showStatus()
    else:
      if index.isdigit():
        choosenFile = splitFiles[int(index)]
        print("git reset" + " " + choosenFile[len("M  "):])
        os.system("git reset" + " " + choosenFile[len("M  "):])
      else:
        output("Index must be an integer!")
    manualMode(index)

# Commit Mode
def commitMode():
  clear()
  inputValue = ""
  msg = ""
  while inputValue != "b":
    clear()
    output("Enter your commit message and end it with '##'")
    output("To exit this commit, include 'exit' in the message")
    inputValue = input("""

Message: {}""".format(msg))
    msg += "{}\n".format(inputValue)
    if "##" in msg:
      msg = msg.replace("##", "")
      os.system("git commit -m " + '"{}"'.format(msg))
      inputValue = "b"
    elif "exit" in msg:
      inputValue = "b"