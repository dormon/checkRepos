#!/usr/bin/python

import externLibraries
import myCmakeLibraries

gits = externLibraries.gits + myCmakeLibraries.gits 

import sys
import os
import argparse
import re
import shutil
import inspect

parser = argparse.ArgumentParser(description='Download/pull all Shadows dependencies, compile and install them.')
parser.add_argument('--threads', type=int, default=4,  help='number of threads for compilation')
parser.add_argument('--dontBuildDebug',action='store_true')
parser.add_argument('--dontBuildRelease',action='store_true')
parser.add_argument('--installDir', type=str, default="../../install", help='where to install all repositories')
parser.add_argument('--separateInstall',action='store_true',help='every library will be installed to separate location')
parser.add_argument("--static"         ,action='store_true',help='build static libraries')
parser.add_argument('--repoDir', type=str, default="..", help='where to download repositories')
parser.add_argument('--dontPull', action='store_true')
parser.add_argument('--clearBuild', action='store_true')

args = parser.parse_args()

threads      = args.threads
buildDebug   = not args.dontBuildDebug
buildRelease = not args.dontBuildRelease
installDir   = args.installDir
repoDir      = args.repoDir
curDir       = os.path.abspath(".")
dontPull     = args.dontPull
clearBuild   = args.clearBuild
separateInstall = args.separateInstall
static          = args.static

system = sys.platform

if not dontPull:
    os.system("python pull.py") 

buildScript = "python buildAndInstall.py --threads "+str(threads)+" --installDir "+str(installDir)+" --repoDir "+str(repoDir)
if not buildDebug:
    buildScript += " --dontBuildDebug "
if not buildRelease:
    buildScript += " --dontBuildRelease "
if clearBuild:
    buildScript += " --clearBuild "
if separateInstall:
    buildScript += " --separateInstall "
if static:
    buildScript += " --static "
os.system(buildScript)
