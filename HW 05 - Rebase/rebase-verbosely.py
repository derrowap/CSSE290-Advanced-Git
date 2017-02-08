#!/usr/bin/python3
"""
Author: Austin Derrow-Pinion
Assignment: Rebase
Date: 01/17/2017

This script takes a single parameter (-b), which is the branch or commit SHA
to rebase to. It will rebase the current state of your local repository to
the provided SHA and print out the new SHA value for each old commit that
was reapplied during the rebase.

NOTE: This script assumes that the rebase goes perfectly with no conflicts.

EXAMPLE:
~/git/js-parsons % git checkout 939a576
HEAD is now at 939a576... Fix output comparison in variablechecking

~/git/js-parsons % rebase-verbosely.py -b 7e64813
git rebase 7e64813
First, rewinding head to replay your work on top of it...
Applying: Fixes to logged data.
Applying: Fix coloring of variable values in variable checker feedback
Applying: Make toggle separator configurable
Applying: Updated Skulpt; new option to turtle grader
Applying: Fix output comparison in variablechecking
939a576 becomes d2bfeb9: Fix output comparison in variablechecking
c72f4a5 becomes f9b9a5f: Updated Skulpt; new option to turtle grader
d2e3233 becomes 4d79fb1: Make toggle separator configurable
ce0b906 becomes 173a726: Fix coloring of variable values in variable checker feedback
283bb73 becomes b4ae363: Fixes to logged data.
7e64813 is the new base: Minor css fixes to prevent misbehaving in some environments

~/git/js-parsons %
"""

import sys
import subprocess

# ensure proper arguments were given
if len(sys.argv) != 3 or sys.argv[1] != '-b':
  print("Must provide a branch or commit SHA like:")
  print("./rebase-verbosely -b 7e64813")

# store history before rebase
sha_comment = [[commit[:7], commit[7:]]
  for commit in subprocess.getoutput("git log --oneline").split('\n')]

# rebase to provided SHA
print("git rebase {}".format(sys.argv[2]))
print(subprocess.getoutput("git rebase {}".format(sys.argv[2])))

# show the new SHA of each old SHA up to the new base
i = 0
for commit in subprocess.getoutput("git log --oneline").split('\n'):
  if commit[:7] == sys.argv[2]:
    print("{} is the new base:{}\n".format(commit[:7], commit[7:]))
    break
  for sha, comment in sha_comment[i:]:
    i += 1
    if commit[7:] == comment:
      print("{} becomes {}:{}".format(sha, commit[:7], commit[7:]))
      break
