"""
subdirfind.py
    Tested with Python 3.6 (Anaconda 5 stack) on Linux Mint 19

//////////////////////////////////////////////////////////////////////////////
Notes
    Authored by: Michael Braine, Physical Science Technician
    PHONE: 301 975 3471
    EMAIL: michael.braine@nist.gov (use this instead)
    July, 2018

//////////////////////////////////////////////////////////////////////////////
Purpose
    search subdirectories for pattern. write to file that can be iterated over

//////////////////////////////////////////////////////////////////////////////
References
    -none

//////////////////////////////////////////////////////////////////////////////
Inputs
    -path - root of directory to search through
    -pattern - pattern to search for

//////////////////////////////////////////////////////////////////////////////
Outputs
    -gits.list -file- list of matches

//////////////////////////////////////////////////////////////////////////////
Change Log from v1.00 to v1.00
    July 4, 2018
    -initial version

//////////////////////////////////////////////////////////////////////////////
"""

import sys
import os

_, path, pattern = sys.argv

with open(path+'/gits.list', mode='w') as openedfile:
    for root, dirs, files in os.walk(path):
        if pattern in dirs:
            openedfile.write(root+'\n')
