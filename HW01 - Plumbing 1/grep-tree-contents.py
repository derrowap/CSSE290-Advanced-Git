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
import os

print("Number of arguments: {}".format(len(sys.argv)))
print("Argument List: {}".format(str(sys.argv)))

tree_sha = ""
search_term = ""

if sys.argv[1] == "-t":
  tree_sha = sys.argv[2]
  search_term = sys.argv[4]
else:
  tree_sha = sys.argv[4]
  search_term = sys.argv[2]

print("tree_sha = {}".format(tree_sha))
print("search_term = {}".format(search_term))

print(os.system("git cat-file -p master^{tree}"))
# print(os.system("git hash-object ../HW01\ -\ Plumbing\ 1"))
# print(os.system("git cat-file -p 56f4f9a11158ee3a93c2df940df667d16d9bd6e1"))