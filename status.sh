#!/usr/bin/env bash
for i in `cat ~/node_list`; do ssh $i "tail -n 1 ~/radargun/stdou*"; done 2> /dev/null
