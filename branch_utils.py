import os
from utils import showStatus, clear, output, manualMode, extraOptions

# Variables
stepOptions = "(b)-back a step | (e)-exit branch mode"

types = [
  "build",
  "ci",
  "docs",
  "feat",
  "fix",
  "perf",
  "refactor",
  "style",
  "test"
]

# Utils

# Get Index Branchs
def getIndexedBranches(branches):
  options = ""
  for index, branch in enumerate(branches):
    if branch != "":
      options += "[{}]: {}\n".format(index, branch)
  return options

# Common Command Loop
def commonCmdLoop(opMsg, systemCmd):
  clear()
  index = ""
  while index != "b":
    output(opMsg + " or " + extraOptions)
    branches = os.popen("git branch").read()
    splitBranches = branches.split("\n")
    indexedBranches = getIndexedBranches(splitBranches)
    print(indexedBranches)
    index = input("""

Index: """)
    if index == "t":
      showStatus()
    else:
      if index.isdigit():
        os.system(systemCmd + " " + splitBranches[int(index)])
      else:
        output("Index must be an integer!")
    manualMode(index)

# Create New Branch
def createNewBranch():
  branch_type = ""
  ticket_id = ""
  ticket_name = ""
  joined_name = ""
  branch_name = ""
  step = 1
  while branch_name == "" and step != 0:
    while step == 1:
      clear()
      output("Pick a branch type by index or " + stepOptions)
      for index in range(len(types)):
        print("[{}]: {}".format(index, types[index]))
      index = input("""

Index: """)
      if index == "b":
        step = 0
      elif index == "e":
        step = 0
        branch_name = "exit"
      else:
        branch_type = index
        step = step + 1
    
    while step == 2:
      clear()
      output("Enter your ticket ID or " + stepOptions)
      t_id = input("""

Ticket ID: """)
      if t_id == "b":
        step = 1
      elif t_id == "e":
        step = 0
        branch_name = "exit"
      else:
        ticket_id = t_id
        step = step + 1

    while step == 3:
      clear()
      print("Example: add styles to component")
      output("Enter your ticket name or " + stepOptions)
      t_name = input("""

Ticket Name: """)
      if t_name == "b":
        step = 2
      elif t_name == "e":
        step = 0
        branch_name = "exit"
      else:
        ticket_name = t_name
        step = step + 1

    if ticket_name != "" and ticket_name != "b" and ticket_name != "e":
      split_name = ticket_name.split(" ")
      joined_name = "-".join(split_name)
      branch_name = "{}/{}-{}".format(
        types[int(branch_type)],
        ticket_id,
        joined_name
      )

  if branch_name != "" and branch_name != "exit":
    os.system("git checkout -b " + branch_name)