#!/usr/bin/env bash
for i in `cat ~/slaves`; do echo "##########" ; echo "sfork: $i"; echo "##########"; ssh $i $@; done
