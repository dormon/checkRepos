#!/usr/bin/python

from myRepositories import *

import sys
import os
from subprocess import call
from subprocess import Popen, PIPE
import argparse
import re
import shutil

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
    call(["git","-C",gitDir,"status"])

