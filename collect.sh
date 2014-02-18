FOLDERNAME="../results"

if [ $FOLDERNAME ]; 
then 
    echo "folder $FOLDERNAME exists. copying to unique name!"; 
    FOLDERNAME="../results".`date "+%Y%m%d.%H%M%S"`
fi

for i in `cat ~/slaves`; do mkdir -p $FOLDERNAME/$i; scp $i:~/radargun/* $FOLDERNAME/$i; done
cp -r ~/wpm/log/csv/ $FOLDERNAME/
mkdir -p $FOLDERNAME/config
cp -r wpm $FOLDERNAME/config
cp -r radargun $FOLDERNAME/config
cp -r beforeBenchmark.sh $FOLDERNAME/config

echo "copied results to $FOLDERNAME"
