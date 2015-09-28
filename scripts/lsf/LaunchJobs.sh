#!/bin/bash
# Script to automatize the launching of batches to LSF - A. Santamaria Garcia
# ------------------------------------------------------------------------------

# Enter the number of batches of 500 jobs that you want to send to LSF
read -r -p 'Enter number of batches >>> ' batch

# Create the needed folders, and create a random distribution in each of them
for num in $(seq 1 $batch)
do
    ( cp -r job_template $num && cd $num/distributions && python generate_distribution.py)
done

# Launch the jobs
for d in $(seq 1 $batch)
do
    (cd $d && ./launcher.sh 1nd 500)
done

