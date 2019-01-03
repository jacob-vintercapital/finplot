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

# computer
CLINUX = True

# import data
execfile('py/1_import.py')

# functions
execfile('py/3_f_rescalew.py')
execfile('py/3_f_returns.py')

# clean
#execfile('py/4b-0-transform.py')


# create baskets
execfile('py/4b-1-ggbasket.py')
execfile('py/4b-2-ggbasket-check.py')
execfile('py/4b-3-ggbasket_transf.py')


## create output

#execfile('py/6-bandw.py') # not sure it is correct

execfile('py/7-vcc_ret.py')
execfile('py/7-vcc_vol.py')
execfile('py/7-ret_slides.py')

#execfile('py/8-boke1.py')

execfile('py/9-bsk_wei.py')
execfile('py/9-bsk_ret.py')
execfile('py/9-bsk_statsmodels.py')

