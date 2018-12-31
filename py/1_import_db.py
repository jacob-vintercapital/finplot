import sqlite3
from sqlite3 import Error
import time

## folder

FOLDER_1 = '/home/he2/Dropbox/Axlantic/data/'
FOLDER_2 = 'other/raw/'
FOLDER_3 = '/home/he2/Documents/datasets/vintercapital_mega/'
FILE_1 = 'coinmarketcap.db'
FILE_2 = 'nomics.db'

# make sure path referencing works 
volu1 = pd.read_csv(FOLDER_1 + FOLDER_2 + 'volume_monthly.csv')
volu1.info()

## IndexComposition table

# Create connection
marketcap = sqlite3.connect(FOLDER_3 + FILE_1)
db_nomics = sqlite3.connect(FOLDER_3 + FILE_2)
df1 = pd.read_sql_query("SELECT * FROM coinmarketcap_coin", marketcap)
df2 = pd.read_sql_query("SELECT * FROM coinmarketcap_coin_data", marketcap)

# see
df1.info()
df2.info()

# dates
df1.cdate.min()
df1.cdate.max()

# structure
df1.head(3)
df1.tail(3)