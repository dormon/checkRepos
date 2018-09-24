#!/usr/bin/python


import myNonCmakeRepositories
import myCmakeLibraries
import myCmakeApps

gits = myNonCmakeRepositories.gits + myCmakeLibraries.gits + myCmakeApps.gits

import sys
import os
from subprocess import call
from subprocess import Popen, PIPE
import argparse
import re
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='Performs git status on all git directories.')
parser.add_argument('--repoDir', type=str, default="..", help='where to download repositories')

args = parser.parse_args()

repoDir      = args.repoDir

if not os.path.isabs(repoDir):
    repoDir = os.path.join(os.path.abspath("."),repoDir)

def getGitDirectory(url):
    return url[url.rfind("/")+1:url.rfind(".")]

for i in gits:
    gitDir = os.path.join(repoDir,getGitDirectory(i[0]))
    print(gitDir)
    output = Popen(["git","-C",gitDir,"status"],stdout=PIPE,stderr=PIPE).communicate()[0]
    if output.find("working tree clean") < 0:
        print(bcolors.FAIL + output + bcolors.ENDC)

