#!/bin/bash

echo "Launching job $current of" $last 

#---------------------------------------------------------------------
# Create jobs folder
#---------------------------------------------------------------------
if [ -d  $DIR/results/job_$current ]; then
  rm -r  $DIR/results/job_$current
fi
mkdir $DIR/results/job_$current

#---------------------------------------------------------------------
# Copy the needed files
#---------------------------------------------------------------------
cp $DIR/sixtrack_input/* .
cp /afs/cern.ch/work/a/ansantam/private/2016/new_lattice/commons/* .
cp $DIR/phases/phase_$current .
mv phase_$current crab2

ls -lh

#---------------------------------------------------------------------
# Execute SixTrack and redirect the output to a file
#---------------------------------------------------------------------
./sixtrack_4533_nocoll > log_six.txt
echo "--------------------------"
echo ">>> SixTrack ran! <<<"
echo "--------------------------"
tail log_six.txt

ls -lh

#---------------------------------------------------------------------
# Copy files back
#---------------------------------------------------------------------
cp dump.txt $DIR/results/job_$current
cp dynksets.dat $DIR/results/job_$current
