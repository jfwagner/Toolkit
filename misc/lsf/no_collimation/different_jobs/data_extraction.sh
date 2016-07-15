#!/bin/bash
export DIR=$(pwd)
cd $DIR/1_turn
if [ -d LSF* ]; then
    rm -r LSF*
fi
cd results/
sigma.py $DIR/1_turn/results/ 1
mv pos_data.txt $DIR/1_turn/

cd ../../2_turns/
if [ -d LSF* ]; then
    rm -r LSF*
fi
cd results/
sigma.py $DIR/2_turns/results/ 2
mv pos_data.txt $DIR/2_turns/

cd ../../3_turns/
if [ -d LSF* ]; then
    rm -r LSF*
fi
cd results/
sigma.py $DIR/3_turns/results/ 3
mv pos_data.txt $DIR/3_turns/

cd ../../4_turns/
if [ -d LSF* ]; then
    rm -r LSF*
fi
cd results/
sigma.py $DIR/4_turns/results/ 4
mv pos_data.txt $DIR/4_turns/

cd ../..
find -name "pos_data.txt" | xargs cat > data.txt

plot_sigma.py 1 20

convert -delay 70 -loop 0 *.png y_position.gif

if [ -d position_plots ]; then
    rm -r position_plots
fi

mkdir position_plots
mv *.png position_plots
