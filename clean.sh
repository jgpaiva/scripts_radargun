~/radargun/bin/master.sh -stop
for i in `cat ~/slaves`; do ssh $i "killall java"; done
killall beforeBenchmark.sh
