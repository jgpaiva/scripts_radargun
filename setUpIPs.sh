#!/usr/bin/env bash

set -o errexit  # Exit on simple commands that return non-zero status.
set -o errtrace # Makes shell functions, command substitutions, and 
                # commands in subshells inherit traps on ERR
set -o nounset  # Exit on use of unset variables.

IPS=`nova list | grep -P -o "(?<==).* "`

echo "cloudtm.ist.utl.pt" > ~/node_list
rm ~/slaves

for i in $IPS
do
    echo "$i" >> ~/node_list
    echo -n "$i " >> ~/slaves
done

ONEIP=`tail -n 1 ~/node_list`

perl -p -i -e "s/^VM=.*/VM=$ONEIP:9998/" beforeBenchmark.sh
