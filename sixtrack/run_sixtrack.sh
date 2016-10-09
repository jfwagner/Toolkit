#!/bin/bash
export DIR=$(pwd)
export dist=$1
cp /home/andrea/ansantam_simulations/2016_CC_study_group/normal/commons/* .
# mv init_dist_$dist.txt init_dist.txt
./SixTrack_4538 > log_six.txt
tail log_six.txt
beamlosspattern lowb tracks2.dat test allapert.b1 > log_loss.txt
tail log_loss.txt
perl -pi -e 's/\0/  /g' LPI*
cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositionsHL.b1.dat \
coll_summary.dat > log_clean.txt
tail log_clean.txt
wc -l impacts_real.dat > impacts_real.txt
if [ -d  $DIR/results ]; then
  rm -r  $DIR/results
fi
mkdir $DIR/results
get_losses.py 1
mv tcp.txt tcp_$dist.txt
mv collsys.txt collsys_$dist.txt
mv collimation.txt coll_$dist.txt
mv aperture.txt ap_$dist.txt
cp *.txt results
cp dynksets.dat results
cp collgaps.dat results
cp coll_summary.dat results
cp fort.3 results
rm ./*
