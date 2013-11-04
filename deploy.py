#!/usr/bin/env python

import os
import tempfile
from collections import namedtuple

dryrun=True

ToMove = namedtuple("ToMove",['dest','source'])

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
    if dryrun:
        print command
    else:
        os.system(command)

def createCommand(toSend):
    paths=[]
    for i in toSend:
        paths.extend(getPaths(i.source))

    transformedPaths=[]
    transformedPaths.extend(replacePaths(paths,toSend))

    return transformedPaths

def scpFolder(nodesList,source,target):
    command=" ".join(["parallel-scp -r -h",nodesList,source,target])
    if dryrun:
        print command
    else:
        os.system(command)

#############################################

toSend=[ToMove(dest="../radargun/target/distribution/RadarGun-1.1.0-SNAPSHOT/",source="radargun/"),
        ToMove(dest="../wpm/",source="wpm/"),
        ToMove(dest="../beforeBenchmark.sh",source="beforeBenchmark.sh")]

nodesList="~/node_list"

transformedPaths=createCommand(toSend)

for i in transformedPaths:
    copyFile(i.source,i.dest)

for i in toSend:
    scpFolder(nodesList,i.dest,"~/"+i.source)
