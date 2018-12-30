'''
run this file to get up and running
all objects will be created
no checks will be run (to save time)
this is the minimum viable code needed to run after a new session
hence its name 0start.py
'''

## create objects

# settings
execfile('py/0_lib.py')
execfile('py/0_plots.py')

# pycharm settings
plt.interactive(False)
plt.isinteractive()

# import data
execfile('py/1_import.py')

# functions
execfile('py/3_f_rescalew.py')
execfile('py/3_f_returns.py')
execfile('py/4b-1-ggbasket.py')

# create & export object by applying f() to data
execfile('py/4b-3-ggbasket_transf.py')

## create output

#execfile('py/6-bandw.py') # not sure it is correct

execfile('py/7-vcc_ret.py')
execfile('py/7-vcc_vol.py')
execfile('py/7-ret_slides.py')

#execfile('py/8-boke1.py')

execfile('py/9-bsk_wei.py')
execfile('py/9-bsk_ret.py') # /home/he2/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py:528: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
execfile('py/9-bsk_statsmodels.py')

