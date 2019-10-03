# checkRepos
Simple python scripts for checking, pulling, compiling and installing multiple git projects

# Building
These scripts will download several repositories, build them and install them.
This is how the directories will look in the end:
```
pathToSomewhere/git/checkRepos
pathToSomewhere/git/Vars
pathToSomewhere/git/glm
pathToSomewhere/git/...
pathToSomewhere/install/linux2/lib
pathToSomewhere/install/linux2/include
pathToSomewhere/install/linux2/...
```

You can change directories, look at help of downloadBuildInstall.py script:
```
usage: downloadBuildInstall.py [-h] [--threads THREADS] [--dontBuildDebug]
                               [--dontBuildRelease] [--installDir INSTALLDIR]
                               [--separateInstall] [--static]
                               [--repoDir REPODIR] [--dontPull] [--clearBuild]
                               [--https]

Download/pull all Shadows dependencies, compile and install them.

optional arguments:
  -h, --help            show this help message and exit
  --threads THREADS     number of threads for compilation
  --dontBuildDebug
  --dontBuildRelease
  --installDir INSTALLDIR
                        where to install all repositories
  --separateInstall     every library will be installed to separate location
  --static              build static libraries
  --repoDir REPODIR     where to download repositories
  --dontPull
  --clearBuild
  --https               use https instead of ssh
```


## Prerequisites
It requires python 2.7 or 3.7

## SSH
If you would like to push / make merge requests in the future

$ mkdir git
$ cd git
$ git clone git@github.com:dormon/checkRepos.git
$ cd checkRepos
$ python downloadBuildInstall.py

## HTTPS
If you are not interested in pushing / making merge requests

$ mkdir git
$ cd git
$ git clone https://github.com/dormon/checkRepos.git
$ cd checkRepos
$ python downloadBuildInstall.py --https

