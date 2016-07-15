#!/bin/bash
export DIR=$(pwd)
export current=1
export queue=$1
export last=$2

if [ -d  $DIR/results ]; then
  rm -r  $DIR/results
fi
mkdir $DIR/results

rm -r $DIR/results/*/

while (( current <= last)); do
    bsub -o STDOUT -e /dev/null -M 50 -q $queue -J job_$current job.sh 
    let current=current+1
done
