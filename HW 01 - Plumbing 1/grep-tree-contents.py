#!/usr/bin/python3
"""
Author: Austin Derrow-Pinion
Assignment: Plumbing 1
Date: 12/06/2016

This script takes two command line parameters, a git tree SHA of a local
repo and a string to search for. It will then search all the blobs in the
tree for that particular string and print out lines that match. If it
encounters another sub-tree, it will recursively grep the subtree as well.
"""

import sys
import subprocess

tree_sha = ""
search_term = ""

# exit if tree_sha and search_term are not provided
if len(sys.argv) != 5:
  print("Must enter a tree SHA with -t flag and a search term with -s flag!")
  exit(1)

# load in command line parameters
if sys.argv[1] == "-t":
  tree_sha = sys.argv[2]
  search_term = sys.argv[4]
elif sys.argv[1] == "-s":
  tree_sha = sys.argv[4]
  search_term = sys.argv[2]

cat_file = "git cat-file -p "

def grep(tree_sha):
  """Calls search_file for all blobs under this tree and sub-trees"""
  objects = []
  lines = subprocess.getoutput(cat_file + tree_sha).split("\n")
  for line in lines:
    details = line.split()
    if details[1] == 'tree':
      # obj is a tree, or sub-directory
      grep(details[2])
    else:
      # obj is a blob, or file
      search_file(details[2])

def search_file(file_sha):
  """Prints the entire line for any line in file containing the search_term"""
  lines = subprocess.getoutput(cat_file + file_sha).split("\n")
  for line in lines:
    if search_term in line:
      print(line)

# launch grep
grep(tree_sha)
