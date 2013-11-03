./clean.sh
cp 3benchmark.xml radargun/conf/benchmark.xml; 
for i in `cat ~/slaves`; do scp radargun/conf/benchmark.xml $i:~/radargun/conf/ ; scp beforeBenchmark.sh $i:; done
cp ispn.xml radargun/plugins/infinispan4/conf/ispn.xml 
for i in `cat ~/slaves`; do scp ispn.xml $i:~/radargun/plugins/infinispan4/conf/ispn.xml  ; done
pushd radargun
./bin/benchmark.sh -i 3 `cat ~/slaves`
