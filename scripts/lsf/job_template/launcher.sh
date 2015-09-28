#!/bin/bash
export DIR=$(pwd)
export current=1
export queue=$1

export LSB_JOB_REPORT_MAIL=N 

if [ -z $1 ] || [ -z $2 ]; then
    echo Usage:
    echo ./launcher.sh quename numjobs
    echo Example:
    echo ./launcher.sh 8nh 500
    exit 1
fi

if [ -d  $DIR/results ]; then
  rm -r  $DIR/results
fi
mkdir $DIR/results

#read -r -p 'Enter number of jobs >>> ' last
if [ -n $2 ]; then
    last=$2
fi
export last

#rm -r $DIR/results/*/

while (( current <= last)); do
    bsub -M 50 -q $queue -J job_$current job.sh 
    let current=current+1
done


