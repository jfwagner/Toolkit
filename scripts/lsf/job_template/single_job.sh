#!/bin/bash
export DIR=/afs/cern.ch/project/lhc_mib/cc_sims/sensible_phases/tau_4/job_240

echo $DIR

#---------------------------------------------------------------------
# Create jobs folder
#---------------------------------------------------------------------
if [ -d  $DIR/results ]; then
  rm -r  $DIR/results
fi
mkdir $DIR/results

cp $DIR/* .

#---------------------------------------------------------------------
# Execute SixTrack and redirect the output to a file
#---------------------------------------------------------------------
./sixtrack > log_six.txt
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
./cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositions.b1.dat coll_summary.dat > log_clean.txt
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
cp impacts_real.dat $DIR/results
cp coll_summary.dat $DIR/results
cp collgaps.dat $DIR/results
cp LPI_test.s $DIR/results
cp all_absorptions.dat $DIR/results
cp fort.3 $DIR/results
