```

\sixtrack\
    |
    |------collimation_post_processing.sh
    |------dynk_dipolar_kick.py
    |------dynk_phase_trip.py
    |------dynk_voltage_decay.py
    |------generate_distribution.py
    |------plot_dynksets.py
    |------plot_sigmas.py
    |------plot_sigma_single.py
    |
    |-----------\dump\
    |		   |
    |              |------plot_cc_voltage.py
    |              |------plot_dump.py
    |              |------plot_emittance_tune.py
    |              |------plot_phase_space.py
    |
    |-----------\impacts_real\
		   |
		   |------plot_coll_impacts.py
		   |------plot_losses_all_cases.py
		   |------plot_losses_turn.py
		   |------plot_losses_turn_core_tail.py
		   |------plot_loss_maps.py

\madx\
    |
    |------plot_beams.py


\misc\
    |
    |------calculate_cc_voltage.py
    |------copy_distributions.sh
    |------extract_3d_data.py
    |------plot_detuning.py
    |------populate_folders.sh
    |------sigma_dist.py
    |
    |----------\lsf\
                  |
                  |------launch_batches.sh
                  |------launcher.sh
                  |------send.sh
                  |
		  |-----------\collimation\
				     |
		                     |------get_losses_turn.py
		                     |------job.sh
				     |
				     |----------\different_jobs\
				     |			 |
				     |			 |------data_extraction.sh
				     |
				     |----------\same_jobs\
				     			 |
				    			 |------copy.sh
				    			 |------count.sh
				     			 |------merge.sh
				     			 |------post_simulation.sh
				     			 |------run.sh

```