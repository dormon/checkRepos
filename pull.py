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

parser = argparse.ArgumentParser(description='Performs git clone/pull/checkout on all git directories.')
parser.add_argument('--repoDir', type=str, default="..", help='where to download repositories')

args = parser.parse_args()

repoDir      = args.repoDir

if not os.path.isabs(repoDir):
    repoDir = os.path.join(os.path.abspath("."),repoDir)

def getGitDirectory(url):
    return url[url.rfind("/")+1:url.rfind(".")]

def clone(url,commit = ""):
    gitDir = os.path.join(repoDir,getGitDirectory(i[0]))

    if not os.path.isdir(gitDir):
        print ("cloning: "+gitDir)
        call(["git","-C",reporDir,"clone",url])
    else:
        print ("executing git pull on: "+gitDir)
        call(["git","-C",gitDir,"pull"])

    if commit != "":
        print ("checkout: "+commit)
        call(["git","-C",gitDir,"checkout",commit])

for i in gits:
    clone(i[0],i[1])

