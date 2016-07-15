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
./sixtrack_4533 > log_six.txt
echo "--------------------------"
echo ">>> SixTrack ran! <<<"
echo "--------------------------"
tail log_six.txt

#---------------------------------------------------------------------
# Run BeamLossPattern and redirect the output to a file
#---------------------------------------------------------------------
./beamlosspattern lowb tracks2.dat test allapert.b1 > log_loss.txt
echo "----------------------------"
echo ">>> BeamLossPattern ran! <<<" 
echo "----------------------------"
tail log_loss.txt
perl -pi -e 's/\0/  /g' LPI*

#---------------------------------------------------------------------
# Run CleanInelastic and redirect the output to a file
#---------------------------------------------------------------------
./cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositionsHL.b1.dat coll_summary.dat > log_clean.txt
echo "----------------------------"
echo ">>> CleanInelastic ran! <<<" 
echo "----------------------------"
tail log_clean.txt

#---------------------------------------------------------------------
# Remove heavy files
#---------------------------------------------------------------------
rm tracks2.dat
rm FirstImpacts_AcceleratorFrame.dat
rm fort.45

ls -lh

#cp dump.txt $DIR/results/job_$current
cp impacts_real.dat $DIR/results/job_$current
cp coll_summary.dat $DIR/results/job_$current
cp collgaps.dat $DIR/results/job_$current
cp LPI_test.s $DIR/results/job_$current
cp all_absorptions.dat $DIR/results/job_$current
cp fort.3 $DIR/results/job_$current
cp crab2 $DIR/results/job_$current
cp dynksets.dat $DIR/results/job_$current
