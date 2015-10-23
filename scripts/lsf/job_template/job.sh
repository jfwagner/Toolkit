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
cp $DIR/executables/* .
cp $DIR/distributions/init_dist_$current.txt .
mv init_dist_$current.txt init_dist.txt
# tail init_dist.txt
echo "------------------------------------"
echo ">>> Initial Distribution copied <<<" 
echo "------------------------------------"
ls -lh

#Prepare fort.3
sed 's/THERNGSEEDGOESHERE/'$current'/' fort.3.template > fort.3

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
cp impacts_real.dat $DIR/results/job_$current
cp coll_summary.dat $DIR/results/job_$current
cp collgaps.dat $DIR/results/job_$current
cp LPI_test.s $DIR/results/job_$current
cp all_absorptions.dat $DIR/results/job_$current
cp fort.3 $DIR/results/job_$current
cp dump_ip1.txt $DIR/results/job_$current
cp dynksets.dat $DIR/results/job_$current
