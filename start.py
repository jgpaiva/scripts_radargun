#!/usr/bin/env python

import os
import deploy

numMachines = 3

dryrun=False
deploy.dryrun=dryrun

def clean():
    command= "./clean.sh"
    print command
    if not dryrun:
        os.system(command)

def start():
    command=" ".join(["pushd ~/radargun;./bin/benchmark.sh -i",str(numMachines),"`cat ~/slaves`;popd;pushd ~/wpm;./log_service.sh restart"])
    command='bash -c "'+command+'"'
    print command
    if not dryrun:
        os.system(command)

clean()
deploy.deploy()
start()
