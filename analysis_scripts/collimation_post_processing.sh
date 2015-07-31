beamlosspattern lowb tracks2.dat test allapert.b1 > log_loss.txt
tail log_loss.txt
perl -pi -e 's/\0/  /g' LPI*

sed -i '/^  54/d' coll_summary.dat
sed -i '/^  55/d' coll_summary.dat
sed -i '/^  56/d' coll_summary.dat
sed -i '/^  57/d' coll_summary.dat

cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositions.b1.dat coll_summary.dat > log_clean.txt
tail log_clean.txt
     
       
