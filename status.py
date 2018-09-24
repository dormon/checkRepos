#!/usr/bin/python

from myRepositories import *

#gits = [
##("git@github.com:spurious/SDL-mirror.git"     ,"release-2.0.8",[]),
##("git@github.com:assimp/assimp.git"           ,""             ,["-DASSIMP_BUILD_SAMPLES=OFF","-DASSIMP_BUILD_ASSIMP_TOOLS=OFF","-DASSIMP_BUILD_TESTS=OFF"]),
##("git@github.com:g-truc/glm.git"              ,""             ,["-DGLM_TEST_ENABLE=OFF"]),
#("git@github.com:dormon/SDL2CPP.git"          ,""             ,[]),
#("git@github.com:dormon/imguiDormon.git"      ,""             ,[]),
#("git@github.com:dormon/imguiOpenGLDormon.git",""             ,[]),
#("git@github.com:dormon/imguiSDL2Dormon.git"  ,""             ,[]),
#("git@github.com:dormon/imguiSDL2OpenGL.git"  ,""             ,[]),
#("git@github.com:dormon/geGL.git"             ,""             ,[]),
#("git@github.com:dormon/BasicCamera.git"      ,""             ,[]),
#("git@github.com:dormon/MealyMachine.git"     ,""             ,[]),
#("git@github.com:dormon/TxtUtils.git"         ,""             ,[]),
#("git@github.com:dormon/ArgumentViewer.git"   ,""             ,[]),
#("git@github.com:dormon/Vars.git"             ,""             ,[]),
#("git@github.com:dormon/checkRepos.git"       ,""             ,[]),
#("git@github.com:dormon/prj.git"              ,""             ,[]),
#        ]


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
    call(["git","-C",gitDir,"status"])

