import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
try:
	from metaclass import *
except:
	from metaclass25 import *


fig=figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(222)
ax4=fig.add_subplot(224)

def beamx(b1,b2,ipb1,ipb2):
	tfs_file = twiss(b1)
	sigma=(tfs_file.SIGXD)*1000
	x=(tfs_file.X)*1000 
	s=tfs_file.S - ipb1

	p=x+sigma 		#plus
	m=x-sigma		#minus
	fp=x+5*sigma 	#five plus
	fm=x-5*sigma	#five minus

	ax1.plot(s,x, color='blue', label='Beam 1')
	ax1.plot(s,p, color='blue')
	ax1.plot(s,m, color='blue')
	ax1.plot(s,fp, color='blue')
	ax1.plot(s,fm, color='blue')

	ax1.fill_between(s, p, m, facecolor='blue')
	ax1.fill_between(s, p, fp, facecolor='blue', alpha=0.2)
	ax1.fill_between(s, m, fm, facecolor='blue', alpha=0.2)


	tfs_file = twiss(b2)
	sigma=(tfs_file.SIGXD)*1000
	x=(tfs_file.X)*1000 
	s=tfs_file.S - ipb2
	
	p=x+sigma 		#plus
	m=x-sigma		#minus
	fp=x+5*sigma 	#five plus
	fm=x-5*sigma	#five minus

	ax1.plot(s,x, color='red', label='Beam 2')
	ax1.plot(s,p, color='red')
	ax1.plot(s,m, color='red')
	ax1.plot(s,fp, color='red')
	ax1.plot(s,fm, color='red')

	ax1.fill_between(s, p, m, facecolor='red')
	ax1.fill_between(s, p, fp, facecolor='red', alpha=0.2)
	ax1.fill_between(s, m, fm, facecolor='red', alpha=0.2)

	ax1.set_xlabel(r's(m)')
	ax1.set_ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')
	ax1.set_xlim([-150,150])
	# ax1.set_ylim([-20,20])
	ax1.grid(b=True, which='major',linestyle='--')
	ax1.legend(loc='lower right')

def beamy(b1,b2,ipb1,ipb2):
	tfs_file = twiss(b1)
	sigma=(tfs_file.SIGYD)*1000
	y=(tfs_file.Y)*1000 
	s=tfs_file.S - ipb1
	
	p=y+sigma 		#plus
	m=y-sigma		#minus
	fp=y+5*sigma 	#five plus
	fm=y-5*sigma	#five minus

	ax2.plot(s,y, color='blue', label='Beam 1')
	ax2.plot(s,p, color='blue')
	ax2.plot(s,m, color='blue')
	ax2.plot(s,fp, color='blue')
	ax2.plot(s,fm, color='blue')

	ax2.fill_between(s, p, m, facecolor='blue')
	ax2.fill_between(s, p, fp, facecolor='blue', alpha=0.2)
	ax2.fill_between(s, m, fm, facecolor='blue', alpha=0.2)


	tfs_file = twiss(b2)
	sigma=(tfs_file.SIGYD)*1000
	y=(tfs_file.Y)*1000 
	s=tfs_file.S - ipb2
	
	p=y+sigma 		#plus
	m=y-sigma		#minus
	fp=y+5*sigma 	#five plus
	fm=y-5*sigma	#five minus

	ax2.plot(s,y, color='red', label='Beam 2')
	ax2.plot(s,p, color='red')
	ax2.plot(s,m, color='red')
	ax2.plot(s,fp, color='red')
	ax2.plot(s,fm, color='red')

	ax2.fill_between(s, p, m, facecolor='red')
	ax2.fill_between(s, p, fp, facecolor='red', alpha=0.2)
	ax2.fill_between(s, m, fm, facecolor='red', alpha=0.2)

	ax2.set_xlabel(r's(m)')
	ax2.set_ylabel(r'y(mm), $\sigma_y$, 5 $\sigma_y$')
	ax2.set_xlim([-150,150])
	# ax2.set_ylim([-20,20])
	ax2.grid(b=True, which='major',linestyle='--')
	ax2.legend(loc='lower right')

def beta(inputfile,ipb1):
	tfs_file = twiss(inputfile)
	s=tfs_file.S - ipb1
	bx=tfs_file.BETX
	by=tfs_file.BETY

	ax3.plot(s,bx,color='blue', label=r'$\beta_x$')
	ax3.plot(s,by,color='green', label=r'$\beta_y$')

	ax3.set_xlabel(r's(m)')
	ax3.set_ylabel('Beta functions (m)')
	ax3.grid(b=True, which='major',linestyle='--')
	ax3.legend(loc='lower right')
	ax3.set_xlim([-150,150])
	# ax3.set_ylim([-50,1000])
	# ax3.annotate(r'$\beta^*$=3', xy=(0,3), xytext=(0,50), 
    # textcoords='offset points', ha='center', va='bottom',
    # bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
    # arrowprops=dict(arrowstyle='->',  
    #                 color='black'))

def angle(inputfile,ipb1):
	tfs_file = twiss(inputfile)
	s=tfs_file.S - ipb1
	px=tfs_file.PX*1000000
	py=tfs_file.PY*1000000

	ax4.plot(s,px,color='red', label=r'Effective angle in x')
	ax4.plot(s,py,color='purple', label=r'Effective angle in y')

	ax4.set_xlabel(r's(m)')
	ax4.set_ylabel('Effective angle ($\mu$ rad)')
	ax4.grid(b=True, which='major',linestyle='--')
	ax4.legend(loc='lower right')
	ax4.set_xlim([-150,150])
	# ax4.annotate('py=-1.8 $\mu$rad', xy=(0,-1.8), xytext=(-20,40), 
 #            textcoords='offset points', ha='center', va='bottom',
 #            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
 #            arrowprops=dict(arrowstyle='->',  
 #                            color='black'))
	# ax4.annotate('px=-385 $\mu$rad', xy=(0,-385), xytext=(-20,-80), 
	#             textcoords='offset points', ha='center', va='bottom',
	#             bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
	#             arrowprops=dict(arrowstyle='->',  
	#                             color='black'))  







  
