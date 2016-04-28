#!/bin/bash

lines_coll_sum=$(cat coll_summary.dat | wc -l )
lines_coll_sum_tot=$(cat coll_sum_tot.dat | wc -l )
var_1=$((lines_coll_sum_tot*19968))
particles=$(($var_1/$lines_coll_sum))
echo $particles


