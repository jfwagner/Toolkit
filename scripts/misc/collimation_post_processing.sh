beamlosspattern lowb tracks2.dat test allapert.b1 > log_loss.txt
tail log_loss.txt
perl -pi -e 's/\0/  /g' LPI*

cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositions.b1.dat coll_summary.dat > log_clean.txt
tail log_clean.txt
     
       
