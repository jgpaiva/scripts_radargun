#!/usr/bin/env python

import os
import deploy

numMachines = 4

dryrun = False
deploy.dryrun = dryrun


def runCommand(command):
    print command
    if not dryrun:
        os.system(command)


def clean():
    runCommand("./clean.sh")


def start():
    command = "cd ~/radargun;./bin/benchmark.sh -i \
{0} `cat ~/slaves`;".format(numMachines)
    command = 'bash -c "' + command + '"'
    runCommand(command)

clean()
deploy.deploy()
start()
