# ------------------------------------------------------------------------------

# always
import os
import pandas as pd
import numpy as np

# import databases
import sqlite3
from sqlite3 import Error
import time

# dates
from pandas.tseries.offsets import *

# plotting
import matplotlib.pyplot as plt
import matplotlib.backends as pltb
from bokeh import *
import seaborn as sns

# test ggplot
# http://ggplot.yhathq.com/install.html
# from ggplot import *

# handle many files
import glob

# import stocks
import datetime
import pandas_datareader.data as web

# statistical modelling
import statsmodels.api as sm
import scipy.stats as stats

# options
pd.options.display.max_rows = 20