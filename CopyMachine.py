# @author Vikram.Chawla@Ecrebo 1/11/19
# Simple copy machine to make n copies of a file
# no edge cases covered as needed a quick script to make copies
# basic input validation only applies.

import shutil
import sys

if not (len(sys.argv) == 3):
    print(" *** Run with filename.ext and # of copies desired, as arguments ***");
    print("Example python CopyMachine.py filename.ext 10")
else:
    print("Number of arguments given were : ", len(sys.argv) - 1)
    print("The arguments including script name are: ", str(sys.argv))
    for x in range(int(sys.argv[2])):
        shutil.copyfile(str(sys.argv[1]), f'{x}')
    print("Success creating", sys.argv[2] + " copies of " + str(sys.argv[1]))
