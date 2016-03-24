for num in $(seq 1 4)
do
    ( cd $num* && ./launcher.sh 1nd 360 && cd ..)
done
