FOLDERNAME="../results"

if [ $FOLDERNAME ]; 
then 
    echo "folder $FOLDERNAME exists. copying to unique name!"; 
    FOLDERNAME="../results".`date "+%Y%m%d.%H%M%S"`
fi

for i in `cat ~/slaves`; do mkdir -p $FOLDERNAME/$i; scp -C $i:~/radargun/* $FOLDERNAME/$i; done

for i in `cat ~/slaves`; do mkdir -p $FOLDERNAME/wpmlogs/$i; scp -C $i:~/wpm/*.log $FOLDERNAME/wpmlogs/$i; done
cp ~/wpm/*.log $FOLDERNAME/wpmlogs

mkdir -p $FOLDERNAME/wpm
cp -r ~/wpm/log/* $FOLDERNAME/wpm/

mkdir -p $FOLDERNAME/radargunreports
cp -r ~/radargun/reports/* $FOLDERNAME/radargunreports

mkdir -p $FOLDERNAME/config
cp -r wpm $FOLDERNAME/config
cp -r radargun $FOLDERNAME/config
cp -r beforeBenchmark.sh $FOLDERNAME/config

echo "copied results to $FOLDERNAME"
