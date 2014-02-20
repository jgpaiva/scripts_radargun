#!/usr/bin/env python

import os
from collections import namedtuple

dryrun = False
ToMove = namedtuple("ToMove", ['dest', 'source'])

toSend = [ToMove(
    dest="../radargun/target/distribution/RadarGun-1.1.0-SNAPSHOT/",
    source="radargun/"),
    ToMove(dest="../wpm/", source="wpm/"),
    ToMove(dest="../beforeBenchmark.sh", source="beforeBenchmark.sh")]

nodesList = "~/node_list"
slavesList = "/tmp/slave_list_UNIQUE_NAME"


def runCommand(command):
    print command
    if not dryrun:
        os.system(command)

runCommand("tail -n +2 {0} > {1}".format(nodesList, slavesList))


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
        yield os.path.join("~", p)


def replacePaths(paths, replacements):
    for aFile in paths:
        for replacement in replacements:
            if aFile.startswith(replacement.source):
                yield ToMove(source=aFile,
                             dest=aFile.replace(
                                 replacement.source,
                                 replacement.dest, 1))
                continue


def copyFile(source, dest):
    runCommand("cp {0} {1}".format(source, dest))


def createCommand(toSend):
    paths = []
    for i in toSend:
        paths.extend(getPaths(i.source))

    transformedPaths = []
    transformedPaths.extend(replacePaths(paths, toSend))

    return transformedPaths


def scpFolder(nodesList, source, target):
    runCommand("parallel-ssh -h {0} rm -rf {1}".format(nodesList, target))
    runCommand("parallel-scp -r -h {0} {1} {2}".format(
        nodesList, source, target))


def startWPM(nodesList):
    restartLogService()
    runCommand("parallel-ssh -h {0} \
'cd ~/wpm;./run_cons_prod.sh restart'".format(slavesList))


def restartLogService():
    command = "grep -R 1099 ~/wpm/;cd ~/wpm;"
    command += "./log_service.sh stop;./log/clean.sh;"
    command += "cd ~/wpm;sleep 5;./log_service.sh start"
    command = 'bash -c "' + command + '"'
    runCommand(command)


def deploy():
    transformedPaths = createCommand(toSend)

    for i in transformedPaths:
        copyFile(i.source, i.dest)

    print "config files are now in place"

    for i in toSend:
        scpFolder(nodesList, i.dest, "~/" + i.source)

    scpFolder(nodesList, "ml", "/tmp/ml")  # HACK

    startWPM(nodesList)

    print "all files transferred"

if __name__ == "__main__":
    deploy()
