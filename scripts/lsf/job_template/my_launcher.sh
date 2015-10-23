#!/bin/bash
export DIR=$(pwd)
export current=1
export queue=$1

if [ -d  $DIR/results ]; then
  rm -r  $DIR/results
fi
mkdir $DIR/results

read -r -p 'Enter number of jobs >>> ' last
export last

rm -r $DIR/results/*/

while (( current <= last)); do
    bsub -M 50 -q $queue -J job_$current job.sh 
    let current=current+1
done
