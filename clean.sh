~/radargun/bin/master.sh -stop
#for i in `cat ~/slaves`; do ssh $i "killall java"; done
parallel-ssh -h ~/node_list "killall java"
killall beforeBenchmark.sh
exit 0
