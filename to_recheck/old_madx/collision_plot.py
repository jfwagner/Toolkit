import csv
import sys
from collections import defaultdict
 
import numpy as np
from matplotlib import rc
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy import spatial
 
sys.path.append("../../../python_modules")
from plotting import plot_survey_beams
from plotting import plot_twiss_beams
from metaclass import twiss

#---------------
# Plot the beams
#---------------
plot_twiss_beams(r'twiss_ip5_b1.tfs', r'twiss_ip5_b2.tfs', 'x', 'IP5')
plot_twiss_beams(r'twiss_ip5_b1.tfs', r'twiss_ip5_b2.tfs', 'y', 'IP5')
plot_twiss_beams(r'twiss_ip1_b1.tfs', r'twiss_ip1_b2.tfs', 'x', 'IP1')
plot_twiss_beams(r'twiss_ip1_b1.tfs', r'twiss_ip1_b2.tfs', 'y', 'IP1')

plot_survey_beams(r'twiss_ip5_b1.tfs', r'twiss_ip5_b2.tfs', r'survey_ip5_b1.tfs', r'survey_ip5_b2.tfs', 'IP5')
plot_survey_beams(r'twiss_ip1_b1.tfs', r'twiss_ip1_b2.tfs', r'survey_ip1_b1.tfs', r'survey_ip1_b2.tfs', 'IP1')














