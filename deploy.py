#!/usr/bin/env python

import os
import tempfile
from collections import namedtuple

dryrun=True

ToMove = namedtuple("ToMove",['replace','new'])

def getPaths(root):
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
            if aFile.startswith(replacement.new):
                yield ToMove(new=aFile,replace=aFile.replace(replacement.new,replacement.replace,1))
                continue

def copyFile(source,dest):
    command=" ".join(["mv",source,dest])
    if dryrun:
        print command
    else:
        os.system(command)

def createCommand(toSend):
    paths=[]
    for i in toSend:
        paths.extend(getPaths(i.new))

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

toSend=[ToMove(replace="../radargun/target/distribution/RadarGun-1.1.0-SNAPSHOT/",new="radargun/"),
        ToMove(replace="../wpm/",new="wpm/")]

nodesList="~/node_list"

transformedPaths=createCommand(toSend)

for i in transformedPaths:
    copyFile(i.new,i.replace)

for i in toSend:
    scpFolder(nodesList,i.replace,"~/"+i.new)
