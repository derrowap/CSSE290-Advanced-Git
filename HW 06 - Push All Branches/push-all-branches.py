#!/usr/bin/python3
"""
Author: Austin Derrow-Pinion
Assignment: Push All Branches
Date: 02/08/2017

This script will do exactly what the name suggests... push all the
branches in this local repository to the given remote repository.

To do this, it iterates over all the existing branches in the local
repository. For each branch, it calls "git push <remote> <branch>"
to push the current branch to the remote passed in as an argument.

After this, each branch will be pushed and no other branches will be
modified that aren't included in the branches of the local repository.

"""

import sys
import subprocess

# ensure proper arguments were given
if len(sys.argv) != 3 or sys.argv[1] != '--remote':
  print("Must provide a remote like:")
  print("./push-all-branches.py --remote /tmp/testrepo")

# push each branch included in "git ls-remote --heads"
# for branch in [x.split()[1] for x in subprocess.getoutput("git ls-remote --heads").split('\n')[1:]]:
#   print(subprocess.getoutput("git push {} {}".format(sys.argv[2], branch)))

# push each branch included in "git branch"
for branch in subprocess.getoutput("git branch").split()[1:]:
  print(subprocess.getoutput("git push {} {}".format(sys.argv[2], branch)))
