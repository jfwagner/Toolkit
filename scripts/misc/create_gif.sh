BIN=300
FIRST_TURN=1
LAST_TURN=50

plot_distribution.py dump.txt x xp $FIRST_TURN $LAST_TURN $BIN
plot_distribution.py dump.txt y yp $FIRST_TURN $LAST_TURN $BIN
plot_distribution.py dump.txt x y $FIRST_TURN $LAST_TURN $BIN
plot_distribution.py dump.txt z e $FIRST_TURN $LAST_TURN $BIN

mkdir x_xp
mv *x_xp.png x_xp
cd x_xp
convert -delay 50 -loop 0 *.png x_xp.gif
cd ..

mkdir y_yp
mv *y_yp.png y_yp
cd y_yp
convert -delay 50 -loop 0 *.png y_yp.gif
cd ..

mkdir x_y
mv *x_y.png x_y
cd x_y
convert -delay 50 -loop 0 *.png x_y.gif
cd ..

mkdir z_e
mv *z_e.png z_e
cd z_e
convert -delay 50 -loop 0 *.png z_e.gif
cd ..
