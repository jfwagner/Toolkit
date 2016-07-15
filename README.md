# Beam Dynamics Toolkit README

These tools have been developed to mainly treat and plot the data you get from running [SixTrack](https://github.com/SixTrack) and [MAD-X](http://mad.web.cern.ch/mad/). There are also some tools to send large amounts of SixTrack jobs to the [CERN computer farm](http://information-technology.web.cern.ch/services/batch) (in **Toolkit/misc/lsf/**).

## How does this work?
Scripts are divided into plotting and non-plotting. 

```
------\plot
	|---\madx
	|      |---plot_beams.py
	|
	|---\sixtrack
	       |---plot_cc_voltage.py
	       |---plot_detuning.py
	       |---plot_dump.py
	       |---plot_dynksets.py
	       |---plot_emittance_tune.py
	       |---plot_phase_space.py
	       |---plot_sigma_single.py
	       |---plot_sigmas.py

------\misc
        |---calculate_cc_voltage.py
        |---collimation_post_processing.sh
        |---copy_distributions.sh
        |---create_gif.sh
        |---create_phase_trip.py
        |---create_voltage_decay.py
        |---extract_3d_data.py
        |---generate_distribution.py
        |---get_losses_turn.py
        |---populate_folders.sh
        |---sigma.py
        |---sigma_dist.py
        |
        |---\lsf

```

All of them work by using the classes and functions defined in **util.py**, so make sure you add the repository to your python path:
```bash
export PYTHONPATH="/home/$USER/Toolkit:$PYTHONPATH"
```

The scripts are thought to be available **globally** in your computer, meaning that you don't have to copy them anywhere. For this to happen, you will also need to add the repository folders to your path:
```bash
export PATH="/home/$USER/Toolkit:$PATH"
export PATH="/home/$USER/Toolkit/plot:$PATH"
export PATH="/home/$USER/Toolkit/plot/sixtrack:$PATH"
export PATH="/home/$USER/Toolkit/plot/madx:$PATH"
export PATH="/home/$USER/Toolkit/misc:$PATH"
```

The scripts work with command line arguments, where one inputs the name of the data file and a few other options. Here are some examples:

```bash
plot_dump.py dist_21459.txt 1 50 100
plot_emittance_tune.py dist_21459.txt 50
```
 There is not an exhaustive documentation of this for now, so you'll have to open the script and look at what the command line arguments are.

## Requirements
For the scripts to work you'll need to install a few libraries. These are gathered in the **requirements.txt** file. To install them, just type:


```bash
pip install -r requirements.txt
```

## Credit

Be cool and refer to this repo if you end up using it! :thumbsup:

## Some plots from this repo

<a href="https://github.com/KFubuki/Toolkit/blob/master/img/z_e.gif"><img src="https://github.com/KFubuki/Toolkit/blob/master/img/z_e.gif" align="center" width="500" ></a>

<a href="https://github.com/KFubuki/Toolkit/blob/master/img/mean_vs_turns.png"><img src="https://github.com/KFubuki/Toolkit/blob/master/img/mean_vs_turns.png" align="center" width="500" ></a>

<a href="https://github.com/KFubuki/Toolkit/blob/master/img/loss_maps.png"><img src="https://github.com/KFubuki/Toolkit/blob/master/img/loss_maps.png" align="center" width="500" ></a>

<a href="https://github.com/KFubuki/Toolkit/blob/master/img/fft.png"><img src="https://github.com/KFubuki/Toolkit/blob/master/img/fft.png" align="center" width="500" ></a>