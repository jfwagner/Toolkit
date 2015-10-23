#!/bin/bash
# This script takes care of the post processing of the data acquired by launching jobs in LSF - A. Santamaria Garcia
#-------------------------------------------------------------------------------
# Rename the one digit folders so that the next loop works without regex
for dir in [1-9]; do
    if [ -d $dir ]; then
	(mv $dir 0$dir)
    fi
done 


# Execute the merging script in each of the folders
for d in [0-9][0-9]
do
    ( cd $d && ./post_simulation.sh )
done

# Merge the merged files located in each folder
find -name "imp_real.dat" | xargs cat > impacts_real.dat
find -name "aperture.dat" | xargs cat > LPI.s
find -name "coll_sum.dat" | xargs cat > coll_sum_tot.dat
find -name "dump.txt" | xargs cat > dump_ip1.txt

# Copy some needed files
cp 01/results/job_1/coll_summary.dat .
cp 01/results/job_1/collgaps.dat .
cp 01/sixtrack_input/CollPositions.b1.dat .

# Find the total number of particles simulated and print it
lines_coll_sum=$(cat coll_summary.dat | wc -l )
lines_coll_sum_tot=$(cat coll_sum_tot.dat | wc -l )
var_1=$((lines_coll_sum_tot*6400))
particles=$(($var_1/$lines_coll_sum))
echo $particles

# Plot
plot_loss_maps.py LPI.s impacts_real.dat coll_summary.dat CollPositions.b1.dat $particles
plot_coll.py impacts_real.dat 53 TCTVA.4L1.B1 vertical 14.41 $particles
# plot_coll.py impacts_real.dat 55 TCTVA.5L1.B1 vertical 3.17 $particles

# Generate FLUKA input
awk '$1==53 {print $0}' impacts_real.dat >| tctv4.txt
