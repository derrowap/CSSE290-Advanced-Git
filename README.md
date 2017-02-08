# CSSE290-Advanced-Git
CSSE 290 - Advanced Git (Rose-Hulman Institute of Technology)

* HW01 - Plumbing 1
  * grep-tree-contents.py
    * Pass a git tree sha and a search term
  * results.txt
    * Results for js-parsons tree sha: "python3 ../grep-tree-contents -t 7d3b207 -s NOTE > results.txt"
* HW 02 - Plumbing 2
  * alternate-history.py
    * This script takes a series of trees and an output branch. It will create an
    alternate fake history starting with the first tree, going to the second, etc.
    The fake history will be placed in a branch with the given name.
  * results.txt
    * Example output.
* HW 03 - Reset and Hash
  * oneStepBack
    * This script takes the recent changes to the repo and moves them all 1 step back.
    Head becomes the previous commit.
    What was last commit before the script was run becomes staged changed to the head.
    What changes were staged before the script was run should become unstaged.
    Any unstaged changes before the script was run should be stashed.
  * revertExceptFile
    * This script takes two parameters, the SHA of a particular commit and a
    filename. It will reset the git repo completely to a particular commit,
    except for the given filename. That file will be listed as an untracked
    change after the script is run.
  * smashLastTwo
    * This script takes the last 2 commits to the repo, smashes them together
    into a single commit and then commits that. The current head then points
    to the newly created commit. It will then restore any staged or unstaged
    changes so that the current state seems unmodified (except of course the
    history is different).
* HW 04 - Merge
  * auto-merge-with-comments.py
    * This script merges two branches together. If there are any merge conflicts,
    it resolves the conflict by using the current version as the correct version
    and including it unmodified, but including the other version as comment in
    the source code.
  * output.txt
    * Example diff results from running this script.
* HW 05 - Rebase
  * rebase-verbosely.py
    * This script takes a single parameter (-b), which is the branch or commit SHA
    to rebase to. It will rebase the current state of your local repository to
    the provided SHA and print out the new SHA value for each old commit that
    was reapplied during the rebase.
    * NOTE: This script assumes that the rebase goes perfectly with no conflicts.
  * output.txt
    * Example output.
* HW 06 - Push All Branches
  * push-all-branches.py
    * This script will do exactly what the name suggests... push all the
    branches in this local repository to the given remote repository.
