#!/bin/bash

LOG=~/log.out
FIRST_SLEEP=10
SLEEP=60
VM=172.31.0.94:9998
round=0

log() {
echo $1 >> ${LOG}
}

saveMlRules() {
log "Save Machine Learner Rules"
#ssh vm47 "mkdir ~/round-${round}; cp /tmp/ml/input* ~/round-${round}";
#round=`echo "${round}+1" | bc`
}


dataplacement() {
saveMlRules
log "Send data placement request to $VM"
~/radargun/bin/dataPlacement.sh $VM >> ${LOG} 2>&1
}

block() {
log "Sleeping ${SLEEP} seconds"
sleep ${SLEEP}
}

sblock() {
log "Sleeping ${FIRST_SLEEP} seconds"
sleep ${FIRST_SLEEP}
}

monitor() {
log "Restart Csv Reporter"
~/csv-reporter/csvReporter.sh -stop
~/csv-reporter/csvReporter.sh -start
}

stop() {
log "Stop benchmark"
~/radargun/bin/stopBenchmark.sh `cat /home/jgpaiva/node_list` >> ${LOG} 2>&1
}

touch ${LOG}
date > ${LOG}

sblock
#monitor

block

for i in {1..220}; do
dataplacement
block
done

stop

exit 0
