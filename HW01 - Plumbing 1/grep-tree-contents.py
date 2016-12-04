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

if sys.argv[1] == "-t":
  tree_sha = sys.argv[2]
  search_term = sys.argv[4]
else:
  tree_sha = sys.argv[4]
  search_term = sys.argv[2]

cat_file = "git cat-file -p "

def grep(tree_sha):
  """Sea
  """
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
  lines = subprocess.getoutput(cat_file + file_sha).split("\n")
  for line in lines:
    if search_term in line:
      print(line)

grep(tree_sha)
