#!/usr/bin/python3
"""
Author: Austin Derrow-Pinion
Assignment: Plumbing 2
Date: 12/13/2016

This script takes a series of trees and an output branch. It will create an
alternate fake history starting with the first tree, going to the second, etc.
The fake history will be placed in a branch with the given name.
"""

import sys
import subprocess

def commit(tree, parent, message):
  if parent == "":
    return subprocess.getoutput("git commit-tree {} -m \"{}\"".format(
      tree, message))
  return subprocess.getoutput("git commit-tree {} -p {} -m \"{}\"".format(
    tree, parent, message))

trees = []
output_branch = ""

# exit if proper values aren't passed
if len(sys.argv) < 7:
  print("Must enter a series of tree SHA values with -t flag and an output \
    branch name with -o flag")
  exit(1)

# load in command line parameters
for i in range(2, len(sys.argv) - 2, 2):
  trees = trees[:] + [sys.argv[i]]
output_branch = sys.argv[len(sys.argv) - 1]

# commit left to right
last_commit = commit(trees[0], "", "alternative begin")
for tree in trees[1:]:
  last_commit = commit(tree, last_commit, "alternative followup")

subprocess.getoutput("git update-ref refs/heads/{} {}".format(
  output_branch, last_commit))
