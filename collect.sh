for i in `cat ~/slaves`; do mkdir -p ../results/$i; scp $i:~/radargun/* ../results/$i; done
cp -r ~/wpm/log/csv/ ../results/
mkdir -p ../results/config
cp -r wpm ../results/config
cp -r radargun ../results/config
cp -r beforeBenchmark.sh ../results/config

