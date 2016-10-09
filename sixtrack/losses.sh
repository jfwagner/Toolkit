#!/bin/bash
export dist=$1
export items=$2
numdirs=$(find . -maxdepth 2 -type d -exec bash -c "echo -ne '{} '; ls '{}' | wc -l" \; | awk '$NF == '$items''| wc -l)
echo $numdirs 
find results -name "impacts_real.dat" | xargs cat > imp_real.dat
find results -name "LPI_test.s" | xargs cat > lpi.s
mv imp_real.dat impacts_real.dat
mv lpi.s LPI_test.s
get_losses.py $numdirs
ls
mv tcp.txt tcp_$dist.txt
mv collsys.txt collsys_$dist.txt
mv collimation.txt coll_$dist.txt
mv aperture.txt ap_$dist.txt
