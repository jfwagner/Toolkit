#!/bin/bash
# This script merges the relevant files inside the batch folders, and point to the missing jobs - A. Santamaria Garcia
# ------------------------------------------------------------------------------ 

# Remove output folders with STOUT
rm -r LSF*

# Concatenate relevant files inside the batch folders
find results -name "impacts_real.dat" | xargs cat > imp_real.dat
find results -name "LPI_test.s" | xargs cat > aperture.dat
find results -name "coll_summary.dat" | xargs cat > coll_sum.dat
find results -name "dump_ip1.txt" | xargs cat > dump.txt

# Copy back any coll_summary, assuming the first job worked
cp results/job_1/coll_summary.dat .

# Calculate the number of lines the merged file whould have
lines_coll_sum=$(cat coll_summary.dat | wc -l )
lines_coll=$(cat coll_sum.dat | wc -l )
lines_tot=$((lines_coll_sum*500))

# Tell the user which jobs are missing
if [ "$lines_coll" -ne "$lines_tot" ]; then
    folder=${PWD##*/}
    echo 'Missing jobs in folder' $folder
fi

for i in $folder; do
    for num in $(seq 1 500); do
	if [ ! -f ../$i/results/job_$num/coll_summary.dat ]; then
	    echo ">> Not found job" $num
	fi
    done
done
