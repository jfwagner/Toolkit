rm -r LSF*
find results -name "impacts_real.dat" | xargs cat > imp_real.dat
find results -name "LPI_test.s" | xargs cat > aperture.dat
find results -name "coll_summary.dat" | xargs cat > coll_sum.dat
wc -l coll_sum.dat
