#!/usr/bin/env python

import os
import deploy

numMachines = 40

dryrun=False
deploy.dryrun=dryrun

def clean():
    command= "./clean.sh"
    print command
    if not dryrun:
        os.system(command)

def start():
    command=" ".join(["grep -R 1099 ~/wpm/;cd ~/wpm;./log_service.sh stop;./log/clean.sh;cd ~/radargun;./bin/benchmark.sh -i",str(numMachines),"`cat ~/slaves`;cd ~/wpm;sleep 5;./log_service.sh start"])
    command='bash -c "'+command+'"'
    print command
    if not dryrun:
        os.system(command)

clean()
deploy.deploy()
start()
