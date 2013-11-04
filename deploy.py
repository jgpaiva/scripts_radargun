#!/usr/bin/env python

import os
import tempfile
from collections import namedtuple

ToMove = namedtuple("ToMove",['replace','new'])

toSend=[("../radargun/target/distribution/RadarGun-1.1.0-SNAPSHOT","radargun"),("../wpm","wpm")]
nodesFile="~/node_list"

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

def replacePaths(paths,toSend):
    for i in paths:
        for j in toSend:
            if i.startswith(j[1]):
                yield (i,i.replace(j[1],j[0],1))
                continue

                    

paths=[]
for i in toSend:
    paths.extend(getPaths(i[1]))

transformedPaths=[]
transformedPaths.extend(replacePaths(paths,toSend))

print transformedPaths

