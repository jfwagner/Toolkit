#!/bin/bash
export DIR=$(pwd)


cd $DIR/1_turn
rm -rf LSF*
cd results/
# sigma_dist.py $DIR/1_turn/results/ 1
# mv pos_data.txt $DIR/1_turn/
extract_3d_data.py $DIR/1_turn/results/ 1 19968
mv 3d_data.txt $DIR/1_turn/

cd ../../2_turns/
rm -rf LSF*
cd results/
# sigma_dist.py $DIR/2_turns/results/ 2
# mv pos_data.txt $DIR/2_turns/
extract_3d_data.py $DIR/2_turns/results/ 2 19968
mv 3d_data.txt $DIR/2_turns/

cd ../../3_turns/
rm -rf LSF*
cd results/
# sigma_dist.py $DIR/3_turns/results/ 3
# mv pos_data.txt $DIR/3_turns/
extract_3d_data.py $DIR/3_turns/results/ 3 19968
mv 3d_data.txt $DIR/3_turns/

cd ../../4_turns/
rm -rf LSF*
cd results/
# sigma_dist.py $DIR/4_turns/results/ 4
# mv pos_data.txt $DIR/4_turns/
extract_3d_data.py $DIR/4_turns/results/ 4 19968
mv 3d_data.txt $DIR/4_turns/

cd ../..
# find -name "pos_data.txt" | xargs cat > dump_data.txt
find -name "3d_data.txt" | xargs cat > imp_real_data.txt

plot_3d.py

# plot_sigma.py 1 20

# convert -delay 70 -loop 0 *.png y_position.gif

# if [ -d position_plots ]; then
#     rm -r position_plots
# fi

# mkdir position_plots
# mv *.png position_plots
