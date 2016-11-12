#!/usr/bin/env bash

#Stop on error
set -e

if [ $# -ne 5 ]; then
    echo "Usage: post_processing.sh {B1|B2} turns failTurn getLossTurn 'title'"
    exit
fi

export beam=$1
export turns=$2
export failTurn=$3
export getLossTurn=$4
export title=$5

#### CORE ####
cd core
echo "********* CORE *********"

set +e #it's OK to fail deleting files
rm *.txt
rm *.eps
rm *.png
rm *.dat
rm *.s
set -e

find -maxdepth 2 -mindepth 1 -type d -empty -exec echo {} is empty. \;
empty=$(find -maxdepth 2 -mindepth 1 -type d -empty| wc -l)
total=$(find . -mindepth 1 -type d | wc -l)
let total=total-1 # Don't count the "results" folder itself
full=$((total-empty))
echo "total="$total
echo "full="$full
echo "empty="$empty
find results -name "impacts_real.dat" | xargs cat > imp_real.dat
mv imp_real.dat impacts_real.dat
find results -name "LPI_test.s" | xargs cat > LPI.s
mv LPI.s LPI_test.s
if [ -s results/job_1/coll_summary.dat ]; then
    cp results/job_1/coll_summary.dat .
    if ! [ -s fort.3 ]; then
	ln -s results/job_1/fort.3 .
    fi
elif [ -s results/job_2/coll_summary.dat ]; then
    cp results/job_2/coll_summary.dat .
    if ! [ -s fort.3 ]; then
	ln -s results/job_1/fort.3 .
    fi
else
    echo "Didn't find coll_summary.dat in job_1 or job_2..."
    exit
fi
if [ -d ../../commons_$beam ]; then
    cp ../../commons_$beam/CollPositions*.dat .
else
    cp ../../commons/CollPositions*.dat .
fi
get_losses.py $full $turns $beam $failTurn
plot_lossmap.py $beam "$title" $getLossTurn

#### TAIL ####
cd ../tail
echo "********* TAIL *********"

set +e
rm *.txt
rm *.eps
rm *.png
rm *.dat
rm *.s
set -e

find -maxdepth 2 -mindepth 1 -type d -empty -exec echo {} is empty. \;
empty=$(find -maxdepth 2 -mindepth 1 -type d -empty| wc -l)
total=$(find . -mindepth 1 -type d | wc -l)
let total=total-1 # Don't count the "results" folder itself
full=$((total-empty))
echo "total="$total
echo "full="$full
echo "empty="$empty
find results -name "impacts_real.dat" | xargs cat > imp_real.dat
mv imp_real.dat impacts_real.dat
find results -name "LPI_test.s" | xargs cat > LPI.s
mv LPI.s LPI_test.s
if [ -s results/job_1/coll_summary.dat ]; then
    cp results/job_1/coll_summary.dat .
    if ! [ -s fort.3 ]; then
	ln -s results/job_1/fort.3 .
    fi
elif [ -s results/job_2/coll_summary.dat ]; then
    cp results/job_2/coll_summary.dat .
    if ! [ -s fort.3 ]; then
	ln -s results/job_1/fort.3 .
    fi
elif [ -s results/job_3/coll_summary.dat ]; then
    cp results/job_3/coll_summary.dat .
    if ! [ -s fort.3 ]; then
	ln -s results/job_1/fort.3 .
    fi
else
    echo "Didn't find coll_summary.dat in job_1 or job_2 or job_3..."
    exit
fi
if [ -d ../../commons_$beam ]; then
    cp ../../commons_$beam/CollPositions*.dat .
else
    cp ../../commons/CollPositions*.dat .
fi
# python ../postScripts/get_losses.py $full
# python ../postScripts/plot_lossmap.py
get_losses.py $full $turns $beam $failTurn
plot_lossmap.py $beam "$title" $getLossTurn

#### OVERALL ####
cd ..
echo "********* OVERALL *********"
set +e #it's OK to fail deleting files
rm *.eps
rm *.png
set -e
plot_lossmap.py $beam "$title" $getLossTurn core tail
