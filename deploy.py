#!/usr/bin/env python

import os
import tempfile
from collections import namedtuple

dryrun=False

ToMove = namedtuple("ToMove",['dest','source'])

toSend=[ToMove(dest="../radargun/target/distribution/RadarGun-1.1.0-SNAPSHOT/",source="radargun/"),
        ToMove(dest="../wpm/",source="wpm/"),
        ToMove(dest="../beforeBenchmark.sh",source="beforeBenchmark.sh") ]

nodesList="~/node_list"


def getPaths(root):
    if os.path.isfile(root):
        yield root

    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)

def getFolders(root):
    for dirname, dirnames, filenames in os.walk(root):
        for subdirname in dirnames:
            yield os.path.join(dirname, subdirname)

def transformPaths(paths):
    for p in paths:
        yield os.path.join("~",p)

def replacePaths(paths,replacements):
    for aFile in paths:
        for replacement in replacements:
            if aFile.startswith(replacement.source):
                yield ToMove(source=aFile,dest=aFile.replace(replacement.source,replacement.dest,1))
                continue

def copyFile(source,dest):
    command=" ".join(["cp",source,dest])
    print command
    if not dryrun:
        os.system(command)

def createCommand(toSend):
    paths=[]
    for i in toSend:
        paths.extend(getPaths(i.source))

    transformedPaths=[]
    transformedPaths.extend(replacePaths(paths,toSend))

    return transformedPaths

def scpFolder(nodesList,source,target):
    command=" ".join(["parallel-ssh -h",nodesList,"rm -rf",target])
    print command
    if not dryrun:
        os.system(command)
    command=" ".join(["parallel-scp -r -h",nodesList,source,target])
    print command
    if not dryrun:
        os.system(command)

def deploy():
    transformedPaths=createCommand(toSend)

    for i in transformedPaths:
        copyFile(i.source,i.dest)

    print "config files are now in place"

    for i in toSend:
        scpFolder(nodesList,i.dest,"~/"+i.source)

    scpFolder(nodesList,"ml","/tmp/ml") #HACK

    print "all files transferred"
    
if __name__ == "__main__":
    deploy()
