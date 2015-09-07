import sys
import re

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

sys.path.append("../python_modules")
from metaclass import twiss


# List of elements you want to include in plot
#-----------------------------------------------
regex_list = ['ZXD']

# Color options
#--------------
D   = '#419AD9'        # Dipoles: MBX, MBXW, MBRC, MBRS, MBW, MBRB
Q1  = '#249A27'        # MQXA
Q2  = '#55E058'        # MQXB
M   = '#EEBE4C'        # Kickers & Correctors: MC, MK
B   = '#9342AE'        # Beam Instrumentation: B
V   = '#A1AAA2'        # Vacuum elements
TC  = '#EE634C'        # Collimators
TAN = '#8C3C2F'        # TAN & TAS
# spec='#9342AE'       # Spectrometers & compensators: MBAW, MBLW, MBWMD, MBXWH

def plot_twiss_beams(twiss_b1, twiss_b2, coordinate, ip):
    ip_name = '%s'%ip

    twiss_b1 = twiss(twiss_b1)
    twiss_b2 = twiss(twiss_b2)

    s_twiss_b1 = (twiss_b1.S)
    s_twiss_b2 = (twiss_b2.S)

    name_b1 = twiss_b1.NAME
    l_b1 = twiss_b1.L
    aper_1_b1 = (twiss_b1.APER_1)*1000
    aper_2_b1 = (twiss_b1.APER_2)*1000
    aper_3_b1 = (twiss_b1.APER_3)*1000
    aper_4_b1 = (twiss_b1.APER_4)*1000

    name_b2 = twiss_b2.NAME
    l_b2 = twiss_b2.L
    aper_1_b2 = (twiss_b2.APER_1)*1000
    aper_2_b2 = (twiss_b2.APER_2)*1000
    aper_3_b2 = (twiss_b2.APER_3)*1000
    aper_4_b2 = (twiss_b2.APER_4)*1000

    length_acc = 26658.8832

    s_tot_b1 = []
    for item in s_twiss_b1:
        if item < (length_acc / 2):
          s_tot_b1.append(item)
        if item >= (length_acc / 2):
          s_tot_b1.append(item - length_acc)
    
    s_tot_b2 = []
    for item in s_twiss_b2:
        if item < (length_acc / 2):
          s_tot_b2.append(item)
        if item >= (length_acc / 2):
          s_tot_b2.append(item - length_acc)

    #-----------------------------------------------------------------------------------------
    # X
    #-----------------------------------------------------------------------------------------
    if coordinate == 'x':

        #--------------------------------------------------------------------------------------
        # BEAM 1
        #--------------------------------------------------------------------------------------
        x_twiss_b1 = (twiss_b1.X)
        sigmax_twiss_b1 = (twiss_b1.SIGXD)

        x_b1 = []
        sigmax_b1 = []
        s_b1 = []
        aper1_b1 = []
        aper3_b1 = []
        nameb1 = []
        lb1 = []
        zipped_b1 = zip(x_twiss_b1, sigmax_twiss_b1, s_tot_b1, aper_1_b1, aper_3_b1, name_b1, l_b1)
        sorted_zip_b1 = sorted(zipped_b1,key = lambda t: t[2])
        for e1, e2, e3, e4, e5, e6, e7 in sorted_zip_b1: 
          if abs(e3) < 400:
            x_b1.append(e1)
            sigmax_b1.append(e2)
            s_b1.append(e3)
            aper1_b1.append(e4)
            aper3_b1.append(e5)
            nameb1.append(e6.strip('"'))
            lb1.append(e7)

        x_tot_b1 = [(x_b1[i])*1000 for i in range(len(x_b1))]
        x_sigma_b1 = [(x_b1[i] + sigmax_b1[i])*1000 for i in range(len(x_b1))]
        x_msigma_b1 = [(x_b1[i] - sigmax_b1[i])*1000 for i in range(len(x_b1))]
        x_fsigma_b1 = [(x_b1[i] + 5*sigmax_b1[i])*1000 for i in range(len(x_b1))]
        x_mfsigma_b1 = [(x_b1[i] - 5*sigmax_b1[i])*1000 for i in range(len(x_b1))]

        aperture_b1 = []
        y_b1_p = []
        x_b1_p = []
        for e1, e2, e3, e4 in zip(aper1_b1, aper3_b1, x_tot_b1, s_b1):
            if e1 <= e2:
                if e1 < 9999 and e1 != 0:
                    aperture_b1.append(e1)
                    y_b1_p.append(e3)
                    x_b1_p.append(e4)
            elif e1 > e2:
                if e2 < 9999 and e2 != 0:
                    aperture_b1.append(e2)
                    y_b1_p.append(e3)
                    x_b1_p.append(e4)

        y_b1 = [y_b1_p[i] + aperture_b1[i] for i in range(len(y_b1_p))]
        ym_b1 = [y_b1_p[i] - aperture_b1[i] for i in range(len(y_b1_p))]

        #--------------------------------------------------------------------------------------
        # BEAM 2
        #--------------------------------------------------------------------------------------
        x_twiss_b2 = (twiss_b2.X)
        sigmax_twiss_b2 = (twiss_b2.SIGXD)

        x_b2 = []
        sigmax_b2 = []
        s_b2 = []
        aper1_b2 = []
        aper3_b2 = []
        nameb2 = []
        lb2 = []
        zipped_b2 = zip(x_twiss_b2, sigmax_twiss_b2, s_tot_b2, aper_1_b2, aper_3_b2, name_b2, l_b2)
        sorted_zip_b2 = sorted(zipped_b2,key = lambda t: t[2])
        for e1, e2, e3, e4, e5, e6, e7 in sorted_zip_b2: 
          if abs(e3) < 400:
            x_b2.append(e1)
            sigmax_b2.append(e2)
            s_b2.append(e3)
            aper1_b2.append(e4)
            aper3_b2.append(e5)
            nameb2.append(e6.strip('"'))
            lb2.append(e7)

        x_tot_b2 = [(x_b2[i])*1000 for i in range(len(x_b2))]
        x_sigma_b2 = [(x_b2[i] + sigmax_b2[i])*1000 for i in range(len(x_b2))]
        x_msigma_b2 = [(x_b2[i] - sigmax_b2[i])*1000 for i in range(len(x_b2))]
        x_fsigma_b2 = [(x_b2[i] + 5*sigmax_b2[i])*1000 for i in range(len(x_b2))]
        x_mfsigma_b2 = [(x_b2[i] - 5*sigmax_b2[i])*1000 for i in range(len(x_b2))]

        aperture_b2 = []
        y_b2_p = []
        x_b2_p = []
        for e1, e2, e3, e4 in zip(aper1_b2, aper3_b2, x_tot_b2, s_b2):
            if e1 <= e2:
                if e1 < 9999 and e1 != 0:
                    aperture_b2.append(e1)
                    y_b2_p.append(e3)
                    x_b2_p.append(e4)
            elif e1 > e2:
                if e2 < 9999 and e2 != 0:
                    aperture_b2.append(e2)
                    y_b2_p.append(e3)
                    x_b2_p.append(e4)

        y_b2 = [y_b2_p[i] + aperture_b2[i] for i in range(len(y_b2_p))]
        ym_b2 = [y_b2_p[i] - aperture_b2[i] for i in range(len(y_b2_p))]

        #--------------------------------------------------------------------------------------
        # Treat the aperture data
        #--------------------------------------------------------------------------------------
        X1 = []
        Y1 = []
        my_zip_b1 = sorted(zip(x_b1_p, y_b1), key = lambda t: t[0])

        previous_value_1 = None
        new_list_1 = []
        for value_1 in my_zip_b1:
            if previous_value_1:
                # if value_1 == previous_value_1:
                #     print '{} is repeated'.format(value_1) !Debugging
                if value_1 != previous_value_1:
                    new_list_1.append(value_1)
            previous_value_1 = value_1

        p_value_1 = None
        for item in my_zip_b1:
            if p_value_1:
                # if item[0] == p_value_1:
                #     print '{} bad'.format(item[0]) !Debugging
                if item[0] != p_value_1:
                  X1.append(item[0])
                  Y1.append(item[1])
            p_value_1 = item[0]

        X1M = []
        Y1M = []
        my_zip_b1 = sorted(zip(x_b1_p, ym_b1), key = lambda t: t[0])

        previous_value_1 = None
        new_list_1 = []
        for value_1 in my_zip_b1:
            if previous_value_1:
                # if value_1 == previous_value_1:
                #     print '{} is repeated'.format(value_1) !Debugging
                if value_1 != previous_value_1:
                    new_list_1.append(value_1)
            previous_value_1 = value_1

        p_value_1 = None
        for item in my_zip_b1:
            # print item[0]
            if p_value_1:
                # if item[0] == p_value_1:
                #     print '{} bad'.format(item[0])  !Debugging
                if item[0] != p_value_1:
                  X1M.append(item[0])
                  Y1M.append(item[1])
            p_value_1 = item[0]

        X2M = []
        Y2M = []
        my_zip_b2 = sorted(zip(x_b2_p, ym_b2), key = lambda t: t[0])

        previous_value_2 = None
        new_list_2 = []
        for value_2 in my_zip_b2:
            if previous_value_2:
                # if value_2 == previous_value_2:
                #     print '{} is repeated'.format(value_2) 
                if value_2 != previous_value_2:
                    new_list_2.append(value_2)
            previous_value_2 = value_2

        p_value_2 = None
        for item in my_zip_b2:
            # print item[0]
            if p_value_2:
                # if item[0] == p_value_2:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_2:
                  X2M.append(item[0])
                  Y2M.append(item[1])
            p_value_2 = item[0]


        X2 = []
        Y2 = []
        my_zip_b2 = sorted(zip(x_b2_p, y_b2), key = lambda t: t[0])

        previous_value_2 = None
        new_list_2 = []
        for value_2 in my_zip_b2:
            if previous_value_2:
                # if value_2 == previous_value_2:
                #     print '{} is repeated'.format(value_2)
                if value_2 != previous_value_2:
                    new_list_2.append(value_2)
            previous_value_2 = value_2

        p_value_2 = None
        for item in my_zip_b2:
            # print item[0]
            if p_value_2:
                # if item[0] == p_value_2:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_2:
                  X2.append(item[0])
                  Y2.append(item[1])
            p_value_2 = item[0]

        P1_X = []
        P1_Y = []

        zipped_p1 = zip(X1, Y1, X2, Y2)
        for e1, e2, e3, e4 in zipped_p1:
            if e3 < 0:
                P1_X.append(e3)
                P1_Y.append(e4)
            if  e1 > 0:
                P1_X.append(e1)
                P1_Y.append(e2)
                
        sorted_p1 = sorted(zip(P1_X, P1_Y), key = lambda t: t[0])

        X1_P = []
        Y1_P = []
        for e1, e2 in sorted_p1:
            X1_P.append(e1)
            Y1_P.append(e2)

        P1_XM = []
        P1_YM = []

        zipped_p1 = zip(X1M, Y1M, X2M, Y2M)
        for e1, e2, e3, e4 in zipped_p1:
            if e3 > 0:
                P1_XM.append(e3)
                P1_YM.append(e4)
            if  e1 < 0:
                P1_XM.append(e1)
                P1_YM.append(e2)
                
        sorted_p1 = sorted(zip(P1_XM, P1_YM), key = lambda t: t[0])

        X1_PM = []
        Y1_PM = []
        for e1, e2 in sorted_p1:
            X1_PM.append(e1)
            Y1_PM.append(e2)

        #--------------------------------------------------------------------------------------
        # Plot the beams
        #--------------------------------------------------------------------------------------
        plt.figure()

        plt.plot(X1_P, Y1_P, color = 'white', label = 'Aperture')
        plt.plot(X1_PM, Y1_PM, color = 'white')
        plt.fill_between(X1_P, Y1_P, 500, facecolor='grey', alpha=0.5)
        plt.fill_between(X1_PM, Y1_PM, -200, facecolor='grey',alpha=0.5)

        plt.plot(s_b1, x_tot_b1, color = 'blue', label = 'Beam 1')
        plt.plot(s_b1, x_sigma_b1, color = 'blue')
        plt.plot(s_b1, x_msigma_b1, color = 'blue')
        plt.plot(s_b1, x_fsigma_b1, color = 'blue')
        plt.plot(s_b1, x_mfsigma_b1, color = 'blue')

        plt.fill_between(s_b1, x_sigma_b1, x_msigma_b1, facecolor='blue')
        plt.fill_between(s_b1, x_sigma_b1, x_fsigma_b1, facecolor='blue', alpha=0.2)
        plt.fill_between(s_b1, x_msigma_b1, x_mfsigma_b1, facecolor='blue', alpha=0.2)

        plt.plot(s_b2, x_tot_b2, color = 'red', label = 'Beam 2')
        plt.plot(s_b2, x_sigma_b2, color = 'red')
        plt.plot(s_b2, x_msigma_b2, color = 'red')
        plt.plot(s_b2, x_fsigma_b2, color = 'red')
        plt.plot(s_b2, x_mfsigma_b2, color = 'red')

        plt.fill_between(s_b2, x_sigma_b2, x_msigma_b2, facecolor='red')
        plt.fill_between(s_b2, x_sigma_b2, x_fsigma_b2, facecolor='red', alpha=0.2)
        plt.fill_between(s_b2, x_msigma_b2, x_mfsigma_b2, facecolor='red', alpha=0.2)

        #--------------------------------------------------------------------------------------
        # Plot the elements
        #--------------------------------------------------------------------------------------
        name = []
        position = []
        length = []
        for a in regex_list:
            regex = re.compile(a)
            for a, b, c in zip(nameb1, s_b1, lb1):
                if regex.match(a):
                    name.append(a)
                    position.append(b)
                    length.append(c)

        for s, element, l in zip(position, name, length):
            f = s-l
            plt.annotate(element, xy = (f, 150), xytext = (s, 150), name = 'Verdana', family = 'sans-serif', 
                         weight = 'light', va = 'bottom', ha = 'center', rotation = 90, size = 7)
            plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.3)

        plt.ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')
        plt.xlabel(r's(m)')
        plt.ylim([-200, 300])
        plt.xlim([-200, 200])
        plt.legend(loc = 4, prop = {'size':8})
        plt.grid(b = True, which = 'major', linestyle='--')
        plt.title(ip_name + ' at collision')

        pp = PdfPages('twiss_'+ ip_name +'_x.pdf')
        pp.savefig()
        pp.close()

    #------------------------------------------------------------------------------------------
    # Y
    #------------------------------------------------------------------------------------------
    elif coordinate == 'y':

        #--------------------------------------------------------------------------------------
        # BEAM 1
        #--------------------------------------------------------------------------------------
        y_twiss_b1 = (twiss_b1.Y)
        sigmay_twiss_b1 = (twiss_b1.SIGYD)

        y_b1 = []
        sigmay_b1 = []
        s_b1 = []
        aper2_b1 = []
        aper4_b1 = []
        nameb1 = []
        lb1 = []
        zipped_b1 = zip(y_twiss_b1, sigmay_twiss_b1, s_tot_b1, aper_2_b1, aper_4_b1, name_b1, l_b1)
        sorted_zip_b1 = sorted(zipped_b1,key = lambda t: t[2])
        for e1, e2, e3, e4, e5, e6, e7 in sorted_zip_b1: 
          if abs(e3) < 400:
            y_b1.append(e1)
            sigmay_b1.append(e2)
            s_b1.append(e3)
            aper2_b1.append(e4)
            aper4_b1.append(e5)
            nameb1.append(e6.strip('"'))
            lb1.append(e7)

        y_tot_b1 = [(y_b1[i])*1000 for i in range(len(y_b1))]
        y_sigma_b1 = [(y_b1[i] + sigmay_b1[i])*1000 for i in range(len(y_b1))]
        y_msigma_b1 = [(y_b1[i] - sigmay_b1[i])*1000 for i in range(len(y_b1))]
        y_fsigma_b1 = [(y_b1[i] + 5*sigmay_b1[i])*1000 for i in range(len(y_b1))]
        y_mfsigma_b1 = [(y_b1[i] - 5*sigmay_b1[i])*1000 for i in range(len(y_b1))]

        aperturey_b1 = []
        y_b1_p = []
        s_b1_p = []
        for e1, e2, e3, e4 in zip(aper2_b1, aper4_b1, y_tot_b1, s_b1):
            if e1 <= e2:
                if e1 < 9999 and e1 != 0:
                    aperturey_b1.append(e1)
                    y_b1_p.append(e3)
                    s_b1_p.append(e4)
            elif e1 > e2:
                if e2 < 9999 and e2 != 0:
                    aperturey_b1.append(e2)
                    y_b1_p.append(e3)
                    s_b1_p.append(e4)

        y_b1 = [y_b1_p[i] + aperturey_b1[i] for i in range(len(y_b1_p))]
        ym_b1 = [y_b1_p[i] - aperturey_b1[i] for i in range(len(y_b1_p))]

        #--------------------------------------------------------------------------------------
        # BEAM 2
        #--------------------------------------------------------------------------------------
        y_twiss_b2 = (twiss_b2.Y)
        sigmay_twiss_b2 = (twiss_b2.SIGYD)

        y_b2 = []
        sigmay_b2 = []
        s_b2 = []
        aper2_b2 = []
        aper4_b2 = []
        nameb2 = []
        lb2 = []
        zipped_b2 = zip(y_twiss_b2, sigmay_twiss_b2, s_tot_b2, aper_2_b2, aper_4_b2, name_b2, l_b2)
        sorted_zip_b2 = sorted(zipped_b2,key = lambda t: t[2])
        for e1, e2, e3, e4, e5, e6, e7 in sorted_zip_b2: 
          if abs(e3) < 400:
            y_b2.append(e1)
            sigmay_b2.append(e2)
            s_b2.append(e3)
            aper2_b2.append(e4)
            aper4_b2.append(e5)
            nameb2.append(e6.strip('"'))
            lb2.append(e7)

        y_tot_b2 = [(y_b2[i])*1000 for i in range(len(y_b2))]
        y_sigma_b2 = [(y_b2[i] + sigmay_b2[i])*1000 for i in range(len(y_b2))]
        y_msigma_b2 = [(y_b2[i] - sigmay_b2[i])*1000 for i in range(len(y_b2))]
        y_fsigma_b2 = [(y_b2[i] + 5*sigmay_b2[i])*1000 for i in range(len(y_b2))]
        y_mfsigma_b2 = [(y_b2[i] - 5*sigmay_b2[i])*1000 for i in range(len(y_b2))]

        aperturey_b2 = []
        y_b2_p = []
        s_b2_p = []
        for e1, e2, e3, e4 in zip(aper2_b2, aper4_b2, y_tot_b2, s_b2):
            if e1 <= e2:
                if e1 < 9999 and e1 != 0:
                    aperturey_b2.append(e1)
                    y_b2_p.append(e3)
                    s_b2_p.append(e4)
            elif e1 > e2:
                if e2 < 9999 and e2 != 0:
                    aperturey_b2.append(e2)
                    y_b2_p.append(e3)
                    s_b2_p.append(e4)

        y_b2 = [y_b2_p[i] + aperturey_b2[i] for i in range(len(y_b2_p))]
        ym_b2 = [y_b2_p[i] - aperturey_b2[i] for i in range(len(y_b2_p))]
        
        #--------------------------------------------------------------------------------------
        # Treat the aperture data
        #--------------------------------------------------------------------------------------
        X1 = []
        Y1 = []
        my_zip_b1 = sorted(zip(s_b1_p, y_b1), key = lambda t: t[0])

        previous_value_1 = None
        new_list_1 = []
        for value_1 in my_zip_b1:
            if previous_value_1:
                # if value_1 == previous_value_1:
                #     print '{} is repeated'.format(value_1)
                if value_1 != previous_value_1:
                    new_list_1.append(value_1)
            previous_value_1 = value_1

        p_value_1 = None
        for item in my_zip_b1:
            # print item[0]
            if p_value_1:
                # if item[0] == p_value_1:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_1:
                  X1.append(item[0])
                  Y1.append(item[1])
            p_value_1 = item[0]

        X1M = []
        Y1M = []
        my_zip_b1 = sorted(zip(s_b1_p, ym_b1), key = lambda t: t[0])

        previous_value_1 = None
        new_list_1 = []
        for value_1 in my_zip_b1:
            if previous_value_1:
                # if value_1 == previous_value_1:
                #     print '{} is repeated'.format(value_1)
                if value_1 != previous_value_1:
                    new_list_1.append(value_1)
            previous_value_1 = value_1

        p_value_1 = None
        for item in my_zip_b1:
            if p_value_1:
                # if item[0] == p_value_1:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_1:
                  X1M.append(item[0])
                  Y1M.append(item[1])
            p_value_1 = item[0]

        X2M = []
        Y2M = []
        my_zip_b2 = sorted(zip(s_b2_p, ym_b2), key = lambda t: t[0])

        previous_value_2 = None
        new_list_2 = []
        for value_2 in my_zip_b2:
            if previous_value_2:
                # if value_2 == previous_value_2:
                #     print '{} is repeated'.format(value_2)
                if value_2 != previous_value_2:
                    new_list_2.append(value_2)
            previous_value_2 = value_2

        p_value_2 = None
        for item in my_zip_b2:
            # print item[0]
            if p_value_2:
                # if item[0] == p_value_2:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_2:
                  X2M.append(item[0])
                  Y2M.append(item[1])
            p_value_2 = item[0]

        X2 = []
        Y2 = []
        my_zip_b2 = sorted(zip(s_b2_p, y_b2), key = lambda t: t[0])

        previous_value_2 = None
        new_list_2 = []
        for value_2 in my_zip_b2:
            if previous_value_2:
                # if value_2 == previous_value_2:
                #     print '{} is repeated'.format(value_2)
                if value_2 != previous_value_2:
                    new_list_2.append(value_2)
            previous_value_2 = value_2

        p_value_2 = None
        for item in my_zip_b2:
            if p_value_2:
                # if item[0] == p_value_2:
                #     print '{} bad'.format(item[0])
                if item[0] != p_value_2:
                  X2.append(item[0])
                  Y2.append(item[1])
            p_value_2 = item[0]

        P1_X = []
        P1_Y = []

        zipped_p1 = zip(X1, Y1, X2, Y2)
        for e1, e2, e3, e4 in zipped_p1:
            if e3 < 0:
                P1_X.append(e3)
                P1_Y.append(e4)
            if  e1 > 0:
                P1_X.append(e1)
                P1_Y.append(e2)
                
        sorted_p1 = sorted(zip(P1_X, P1_Y), key = lambda t: t[0])

        X1_P = []
        Y1_P = []
        for e1, e2 in sorted_p1:
            X1_P.append(e1)
            Y1_P.append(e2)

        P1_XM = []
        P1_YM = []

        zipped_p1 = zip(X1M, Y1M, X2M, Y2M)
        for e1, e2, e3, e4 in zipped_p1:
            if e3 > 0:
                P1_XM.append(e3)
                P1_YM.append(e4)
            if  e1 < 0:
                P1_XM.append(e1)
                P1_YM.append(e2)
                
        sorted_p1 = sorted(zip(P1_XM, P1_YM), key = lambda t: t[0])

        X1_PM = []
        Y1_PM = []
        for e1, e2 in sorted_p1:
            X1_PM.append(e1)
            Y1_PM.append(e2)

        #--------------------------------------------------------------------------------------
        # Plot the beams
        #--------------------------------------------------------------------------------------
        plt.figure()

        plt.plot(X1_P, Y1_P, color = 'white', label = 'Aperture')
        plt.plot(X1_PM, Y1_PM, color = 'white')
        plt.fill_between(X1_P, Y1_P, 500, facecolor='grey', alpha=0.5)
        plt.fill_between(X1_PM, Y1_PM, -200, facecolor='grey',alpha=0.5)

        plt.plot(s_b1, y_tot_b1, color = 'blue', label = 'Beam 1')
        plt.plot(s_b1, y_sigma_b1, color = 'blue')
        plt.plot(s_b1, y_msigma_b1, color = 'blue')
        plt.plot(s_b1, y_fsigma_b1, color = 'blue')
        plt.plot(s_b1, y_mfsigma_b1, color = 'blue')

        plt.fill_between(s_b1, y_sigma_b1, y_msigma_b1, facecolor='blue')
        plt.fill_between(s_b1, y_sigma_b1, y_fsigma_b1, facecolor='blue', alpha=0.2)
        plt.fill_between(s_b1, y_msigma_b1, y_mfsigma_b1, facecolor='blue', alpha=0.2)

        plt.plot(s_b2, y_tot_b2, color = 'red', label = 'Beam 2')
        plt.plot(s_b2, y_sigma_b2, color = 'red')
        plt.plot(s_b2, y_msigma_b2, color = 'red')
        plt.plot(s_b2, y_fsigma_b2, color = 'red')
        plt.plot(s_b2, y_mfsigma_b2, color = 'red')

        plt.fill_between(s_b2, y_sigma_b2, y_msigma_b2, facecolor='red')
        plt.fill_between(s_b2, y_sigma_b2, y_fsigma_b2, facecolor='red', alpha=0.2)
        plt.fill_between(s_b2, y_msigma_b2, y_mfsigma_b2, facecolor='red', alpha=0.2)

        #--------------------------------------------------------------------------------------
        # Plot the elements
        #--------------------------------------------------------------------------------------
        name = []
        position = []
        length = []
        for a in regex_list:
            regex = re.compile(a)
            for a, b, c in zip(nameb1, s_b1, lb1):
                if regex.match(a):
                    name.append(a)
                    position.append(b)
                    length.append(c)

        for s, element, l in zip(position, name, length):
            f = s-l
            plt.annotate(element, xy = (f, 150), xytext = (s, 150), name = 'Verdana', family = 'sans-serif', 
                         weight = 'light', va = 'bottom', ha = 'center', rotation = 90, size = 7)
            plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.3)
        plt.ylabel(r'y(mm), $\sigma_y$, 5 $\sigma_y$')
        plt.xlabel(r's(m)')
        plt.ylim([-200, 300])
        plt.xlim([-200, 200])
        plt.legend(loc = 4, prop = {'size':8})
        plt.grid(b = True, which = 'major', linestyle='--')
        plt.title(ip_name + ' at collision')

        pp = PdfPages('twiss_'+ ip_name +'_y.pdf')
        pp.savefig()
        pp.close()

def plot_survey_beams(twiss_b1, twiss_b2, survey_b1, survey_b2, ip):
    ip_name = '%s'%ip

    survey_b1 = twiss(survey_b1)
    survey_b2 = twiss(survey_b2)
    
    z_survey_b1 = survey_b1.Z
    z_survey_b2 = survey_b2.Z

    twiss_b1 = twiss(twiss_b1)
    twiss_b2 = twiss(twiss_b2)

    name_b1 = twiss_b1.NAME
    l_b1 = twiss_b1.L
    aper_1_b1 = (twiss_b1.APER_1)*1000
    aper_2_b1 = (twiss_b1.APER_2)*1000
    aper_3_b1 = (twiss_b1.APER_3)*1000
    aper_4_b1 = (twiss_b1.APER_4)*1000

    name_b2 = twiss_b2.NAME
    l_b2 = twiss_b2.L
    aper_1_b2 = (twiss_b2.APER_1)*1000
    aper_2_b2 = (twiss_b2.APER_2)*1000
    aper_3_b2 = (twiss_b2.APER_3)*1000
    aper_4_b2 = (twiss_b2.APER_4)*1000

    #--------------------------------------------------------------------------------------
    # BEAM 1
    #--------------------------------------------------------------------------------------
    x_survey_b1 = survey_b1.X
    x_twiss_b1 = twiss_b1.X
    sigmax_twiss_b1 = twiss_b1.SIGXD

    xs_b1 = []
    xt_b1 = []
    z_b1 = []
    sigmax_b1 = []
    aper1_b1 = []
    aper3_b1 = []
    nameb1 = []
    lb1 = []
    zipped_b1 = zip(x_survey_b1, x_twiss_b1, z_survey_b1, sigmax_twiss_b1, aper_1_b1, aper_3_b1, name_b1, l_b1)
    sorted_zip_b1 = sorted(zipped_b1,key = lambda t: t[2])
    for e1, e2, e3, e4, e5, e6, e7, e8 in sorted_zip_b1: 
      if abs(e3) < 200 and abs(e1) < 200:
        xs_b1.append(e1)
        xt_b1.append(e2)
        z_b1.append(e3)
        sigmax_b1.append(e4)
        aper1_b1.append(e5)
        aper3_b1.append(e6)
        nameb1.append(e7.strip('"'))
        lb1.append(e8)

    x_tot_b1 = [xs_b1[i] + xt_b1[i] for i in range(len(xt_b1))]
    xs_tot_b1 = [(x_tot_b1[i] + sigmax_b1[i])*1000 for i in range(len(xt_b1))]
    xsm_tot_b1 = [(x_tot_b1[i] - sigmax_b1[i])*1000 for i in range(len(xt_b1))]
    xsf_tot_b1 = [(x_tot_b1[i] + 5*sigmax_b1[i])*1000 for i in range(len(xt_b1))]
    xsmf_tot_b1 = [(x_tot_b1[i] - 5*sigmax_b1[i])*1000 for i in range(len(xt_b1))]

    aperture_b1 = []
    y_b1_p = []
    x_b1_p = []
    for e1, e2, e3, e4 in zip(aper1_b1, aper3_b1, x_tot_b1, z_b1):
        if e1 <= e2:
            if e1 < 9999 and e1 != 0:
                aperture_b1.append(e1)
                y_b1_p.append(e3*1000)
                x_b1_p.append(e4)
        elif e1 > e2:
            if e2 < 9999 and e2 != 0:
                aperture_b1.append(e2)
                y_b1_p.append(e3*1000)
                x_b1_p.append(e4)

    y_b1 = [y_b1_p[i] + aperture_b1[i] for i in range(len(y_b1_p))]
    ym_b1 = [y_b1_p[i] - aperture_b1[i] for i in range(len(y_b1_p))]

    #--------------------------------------------------------------------------------------
    # BEAM 2
    #--------------------------------------------------------------------------------------
    x_survey_b2 = survey_b2.X
    x_twiss_b2 = twiss_b2.X
    sigmax_twiss_b2 = twiss_b2.SIGXD

    xs_b2 = []
    xt_b2 = []
    z_b2 = []
    sigmax_b2 = []
    aper1_b2 = []
    aper3_b2 = []
    nameb2 = []
    lb2 = []
    zipped_b2 = zip(x_survey_b2, x_twiss_b2, z_survey_b2, sigmax_twiss_b2, aper_1_b2, aper_3_b2, name_b2, l_b2)
    sorted_zip_b2 = sorted(zipped_b2,key = lambda t: t[2])
    for e1, e2, e3, e4, e5, e6, e7, e8 in sorted_zip_b2: 
      if abs(e3) < 200 and abs(e1) < 200:
        xs_b2.append(e1)
        xt_b2.append(e2)
        z_b2.append(e3)
        sigmax_b2.append(e4)
        aper1_b2.append(e5)
        aper3_b2.append(e6)
        nameb2.append(e7.strip('"'))
        lb2.append(e8)

    x_tot_b2 = [xs_b2[i] + xt_b2[i] for i in range(len(xt_b2))]
    xs_tot_b2 = [(x_tot_b2[i] + sigmax_b2[i])*1000 for i in range(len(xt_b2))]
    xsm_tot_b2 = [(x_tot_b2[i] - sigmax_b2[i])*1000 for i in range(len(xt_b2))]
    xsf_tot_b2 = [(x_tot_b2[i] + 5*sigmax_b2[i])*1000 for i in range(len(xt_b2))]
    xsmf_tot_b2 = [(x_tot_b2[i] - 5*sigmax_b2[i])*1000 for i in range(len(xt_b2))]

    aperture_b2 = []
    y_b2_p = []
    x_b2_p = []
    for e1, e2, e3, e4 in zip(aper1_b2, aper3_b2, x_tot_b2, z_b2):
        if e1 <= e2:
            if e1 < 9999 and e1 != 0:
                aperture_b2.append(e1)
                y_b2_p.append(e3*1000)
                x_b2_p.append(e4)
        elif e1 > e2:
            if e2 < 9999 and e2 != 0:
                aperture_b2.append(e2)
                y_b2_p.append(e3*1000)
                x_b2_p.append(e4)

    y_b2 = [y_b2_p[i] + aperture_b2[i] for i in range(len(y_b2_p))]
    ym_b2 = [y_b2_p[i] - aperture_b2[i] for i in range(len(y_b2_p))]

    #--------------------------------------------------------------------------------------
    # Treat the aperture data
    #--------------------------------------------------------------------------------------
    X1 = []
    Y1 = []
    my_zip_b1 = sorted(zip(x_b1_p, y_b1), key = lambda t: t[0])

    previous_value_1 = None
    new_list_1 = []
    for value_1 in my_zip_b1:
        if previous_value_1:
            # if value_1 == previous_value_1:
            #     print '{} is repeated'.format(value_1)
            if value_1 != previous_value_1:
                new_list_1.append(value_1)
        previous_value_1 = value_1

    p_value_1 = None
    for item in my_zip_b1:
        # print item[0]
        if p_value_1:
            # if item[0] == p_value_1:
            #     print '{} bad'.format(item[0])
            if item[0] != p_value_1:
              X1.append(item[0])
              Y1.append(item[1])
        p_value_1 = item[0]

    X1M = []
    Y1M = []
    my_zip_b1 = sorted(zip(x_b1_p, ym_b1), key = lambda t: t[0])

    previous_value_1 = None
    new_list_1 = []
    for value_1 in my_zip_b1:
        if previous_value_1:
            # if value_1 == previous_value_1:
            #     print '{} is repeated'.format(value_1)
            if value_1 != previous_value_1:
                new_list_1.append(value_1)
        previous_value_1 = value_1

    p_value_1 = None
    for item in my_zip_b1:
        # print item[0]
        if p_value_1:
            # if item[0] == p_value_1:
            #     print '{} bad'.format(item[0])
            if item[0] != p_value_1:
              X1M.append(item[0])
              Y1M.append(item[1])
        p_value_1 = item[0]

    X2M = []
    Y2M = []
    my_zip_b2 = sorted(zip(x_b2_p, ym_b2), key = lambda t: t[0])

    previous_value_2 = None
    new_list_2 = []
    for value_2 in my_zip_b2:
        if previous_value_2:
            # if value_2 == previous_value_2:
            #     print '{} is repeated'.format(value_2)
            if value_2 != previous_value_2:
                new_list_2.append(value_2)
        previous_value_2 = value_2

    p_value_2 = None
    for item in my_zip_b2:
        # print item[0]
        if p_value_2:
            # if item[0] == p_value_2:
            #     print '{} bad'.format(item[0])
            if item[0] != p_value_2:
              X2M.append(item[0])
              Y2M.append(item[1])
        p_value_2 = item[0]


    X2 = []
    Y2 = []
    my_zip_b2 = sorted(zip(x_b2_p, y_b2), key = lambda t: t[0])

    previous_value_2 = None
    new_list_2 = []
    for value_2 in my_zip_b2:
        if previous_value_2:
            # if value_2 == previous_value_2:
            #     print '{} is repeated'.format(value_2)
            if value_2 != previous_value_2:
                new_list_2.append(value_2)
        previous_value_2 = value_2

    p_value_2 = None
    for item in my_zip_b2:
        # print item[0]
        if p_value_2:
            # if item[0] == p_value_2:
            #     print '{} bad'.format(item[0])
            if item[0] != p_value_2:
              X2.append(item[0])
              Y2.append(item[1])
        p_value_2 = item[0]

    P1_X = []
    P1_Y = []

    zipped_p1 = zip(X1, Y1, X2, Y2)
    for e1, e2, e3, e4 in zipped_p1:
        if e3 < 0:
            P1_X.append(e3)
            P1_Y.append(e4)
        if  e1 > 0:
            P1_X.append(e1)
            P1_Y.append(e2)

    sorted_p1 = sorted(zip(P1_X, P1_Y), key = lambda t: t[0])

    X1_P = []
    Y1_P = []
    for e1, e2 in sorted_p1:
        X1_P.append(e1)
        Y1_P.append(e2)


    P1_XM = []
    P1_YM = []

    zipped_p1 = zip(X1M, Y1M, X2M, Y2M)
    for e1, e2, e3, e4 in zipped_p1:
        if e3 > 0:
            P1_XM.append(e3)
            P1_YM.append(e4)
        if  e1 < 0:
            P1_XM.append(e1)
            P1_YM.append(e2)

    sorted_p1 = sorted(zip(P1_XM, P1_YM), key = lambda t: t[0])

    X1_PM = []
    Y1_PM = []
    for e1, e2 in sorted_p1:
        X1_PM.append(e1)
        Y1_PM.append(e2)

    #--------------------------------------------------------------------------------------
    # Plot the beams
    #--------------------------------------------------------------------------------------
    plt.figure()

    plt.plot(X1_P, Y1_P, color = 'white', label = 'Aperture')
    plt.plot(X1_PM, Y1_PM, color = 'white')
    plt.fill_between(X1_P, Y1_P, 500, facecolor='grey', alpha=0.5)
    plt.fill_between(X1_PM, Y1_PM, -200, facecolor='grey',alpha=0.5)

    plt.plot(z_b1, xs_tot_b1, color = 'blue', label = 'Beam 1')
    plt.plot(z_b1, xsm_tot_b1, color = 'blue')
    plt.plot(z_b1, xsf_tot_b1, color = 'blue')
    plt.plot(z_b1, xsmf_tot_b1, color = 'blue')
    plt.fill_between(z_b1, xs_tot_b1, xsm_tot_b1, facecolor='blue')
    plt.fill_between(z_b1, xs_tot_b1, xsf_tot_b1, facecolor='blue', alpha=0.2)
    plt.fill_between(z_b1, xsm_tot_b1, xsmf_tot_b1, facecolor='blue', alpha=0.2)

    plt.plot(z_b2, xs_tot_b2, color = 'red', label = 'Beam 2')
    plt.plot(z_b2, xsm_tot_b2, color = 'red')
    plt.plot(z_b2, xsf_tot_b2, color = 'red')
    plt.plot(z_b2, xsmf_tot_b2, color = 'red')
    plt.fill_between(z_b2, xs_tot_b2, xsm_tot_b2, facecolor='red')
    plt.fill_between(z_b2, xs_tot_b2, xsf_tot_b2, facecolor='red', alpha=0.2)
    plt.fill_between(z_b2, xsm_tot_b2, xsmf_tot_b2, facecolor='red', alpha=0.2)

    #--------------------------------------------------------------------------------------
    # Plot the elements
    #--------------------------------------------------------------------------------------
    name = []
    position = []
    length = []
    for a in regex_list:
        regex = re.compile(a)
        for a, b, c in zip(nameb1, z_b1, lb1):
            if regex.match(a):
                name.append(a)
                position.append(b)
                length.append(c)

    for s, element, l in zip(position, name, length):
        f = s-l
        plt.annotate(element, xy = (f, 200), xytext = (s, 200), name = 'Verdana', family = 'sans-serif', 
                     weight = 'light', va = 'bottom', ha = 'center', rotation = 90, size = 7)
        plt.bar(s-l, 100, l, 200, color = 'green', edgecolor = 'black', linewidth = '1.7', alpha = 0.3)

    plt.ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')
    plt.xlabel(r'z(m)')
    plt.xlim([-200, 200])
    plt.ylim([-200, 200])
    plt.legend(loc = 4, prop = {'size':8})
    plt.grid(b = True, which = 'major', linestyle='--')
    plt.title(ip_name + ' at collision')

    pp = PdfPages('survey'+ ip_name +'x.pdf')
    pp.savefig()
    pp.close()

