./beamlosspattern lowb tracks2.dat test allapert.b1 > log_loss.txt
lt

./cleaninelastic FLUKA_impacts.dat LPI_test.s CollPositionsHL.b1.dat coll_summary.dat > log_clean.txt
lt

rm -rf x_xp
plot_distribution.py dump.txt x xp 1 20 100
mkdir x_xp
mv *x_xp.png x_xp
cd x_xp
convert -delay 50 -loop 0 *.png x_xp_1_83.gif
cd ..

rm -rf y_yp
plot_distribution.py dump.txt y yp 1 20 100
mkdir y_yp
mv *y_yp.png y_yp
cd y_yp
convert -delay 50 -loop 0 *.png y_yp_1_96_1_83.gif
cd ..

rm -rf x_y
plot_distribution.py dump.txt x y 1 20 100
mkdir x_y
mv *x_y.png x_y
cd x_y
convert -delay 50 -loop 0 *.png x_y_1_83.gif
cd ..

rm -rf z_e
plot_distribution.py dump.txt z e 1 20 100
mkdir z_e
mv *z_e.png z_e
cd z_e
convert -delay 50 -loop 0 *.png z_e_1_83.gif
cd ..

rm -rf z_x
plot_distribution.py dump.txt z x 1 20 100
mkdir z_x
mv *z_x.png z_x
cd z_x
convert -delay 50 -loop 0 *.png z_x_1_83.gif
cd ..

rm -rf z_y
plot_distribution.py dump.txt z y 1 20 100
mkdir z_y
mv *z_y.png z_y
cd z_y
convert -delay 50 -loop 0 *.png z_y_1_83.gif
cd ..

plot_loss_maps.py LPI_test.s impacts_real.dat coll_summary.dat CollPositionsHL.b1.dat 19968

plot_dynksets.py dynksets.dat

# plot_coll.py impacts_real.dat 1 TCLX.4R1.B1 horizontal 0.02137628832 19968
# plot_coll.py impacts_real.dat 2 TCL.5R1.B1 horizontal 0.007584099354 19968
# plot_coll.py impacts_real.dat 3 TCL.6R1.B1 horizontal 0.002808478162 19968
# plot_coll.py impacts_real.dat 54 TCTPH.4L1.B1 horizontal 0.01606304157 19968
# plot_coll.py impacts_real.dat 55 TCTPV.4L1.B1 vertical 0.01026567058 19968
# plot_coll.py impacts_real.dat 52 TCTH.6L1.B1 horizontal 0.007983768641 19968
# plot_coll.py impacts_real.dat 53 TCTV.6L1.B1 vertical 0.003568930477 19968
# plot_coll.py impacts_real.dat 29 TCP.D6L7.B1 vertical 0.001093825692 19968

