#---------------------------------------------------------------------
# Script to automatize the MAD-X simulations
#---------------------------------------------------------------------
# Write the name of the folder in which you want to copy your results
#---------------------------------------------------------------------
cd madx_scripts
ls -l
read -r -p 'Select MAD-X input script from the list above >>> ' folder
cd ..
if [ -d results/$folder ]; then
  sudo rm -r results/$folder
fi
mkdir results/$folder
cd results/$folder
mkdir plots
mkdir input_$folder

#---------------------------------------------------------------------
# Execute your MAD-X script
#---------------------------------------------------------------------
cd ../../madx_scripts
cp $folder ../results/$folder/input_$folder
cd ../results/$folder/input_$folder
madx < $folder >> log.out
tail log.out
echo "--------------------------"
echo ">>> MAD-X ran! <<<"
echo "--------------------------"

#---------------------------------------------------------------------
# Create a different file for each selected element
#---------------------------------------------------------------------
cd ../../../data_treatment
cp collision_plot.py ../results/$folder/input_$folder
cd ../results/$folder/input_$folder
python collision_plot.py 2>&1

#---------------------------------------------------------------------
# Copy to the results folder
#---------------------------------------------------------------------
mv *.pdf ../plots










