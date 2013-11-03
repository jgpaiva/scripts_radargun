./clean.sh
for i in `cat ~/slaves`; do cp 9benchmark.xml radargun/conf/benchmark.xml; scp radargun/conf/benchmark.xml $i:~/radargun/conf/ ; scp beforeBenchmark.sh $i:; done
pushd radargun
./bin/benchmark.sh -i 9 `cat ~/slaves`
