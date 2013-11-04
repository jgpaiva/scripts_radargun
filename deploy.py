#!/usr/bin/env python

import os
import tempfile

toSend=["radargun","wpm"]
nodesFile="~/nodes_list"

def getPaths(root):
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)

def getFolders(root):
    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            yield os.path.join(dirname, subdirname)

def transformPaths(paths):
    for p in paths:
        yield os.path.join("~",p)

def scpToNodes(nodesFile,paths,transformedPaths):
    with tempfile.NamedTemporaryFile() as local:
        with tempfile.NamedTemporaryFile() as remote:
            local.write("\n".join(paths))
            remote.write("\n".join(transformedPaths))
            local.flush()
            remote.flush()
            os.system(" ".join("parallel-scp -h",nodesFile,local.name,remote.name)
                    
def mkdirFilesOnNodes(nodesFile,folders):


folders=[]
for i in toSend:
    folders.extend(getFolders(i))

folders=list(transformedPaths(folders))

mkdirFilesOnNodes(nodesFile,folders)

paths=[]
for i in toSend:
    paths.extend(getPaths(i))

transformedPaths=[]
transformedPaths.extend(transformPaths(paths))

scpToNodes(nodesFile,paths,transformedPaths)
