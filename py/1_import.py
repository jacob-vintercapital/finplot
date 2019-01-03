"""
import data from coins, which has previously been extracted using HH's R script.
saves the imported objects in memory as pandas dataframes.
"""

## start date for reading in data and doin analysis

# userinputchoice
START1 = '2015-04'
END1 = '2018-04'
PC = False

## working dir

print("work dir", os.getcwd())

## f() date as index

def re_index_date(df):
    """
    input df.
    output df reindexed with its .index as daily index ffilled.

    todo hakan, this is needed because pandas complained dates are not regular.
    this led the .freq to not be daily which we need!
    please double check the data you gave me
    so that this resampling does not render calculations incorrect.
    """
    # convert index to datetime
    # assume type(vol_fin_mat.index) is pandas DatetimeIndex
    start_date= min(df.index)
    end_date= max(df.index)
    # set index freq to daily
    dtindex = pd.date_range(start_date, end_date, freq='D')
    df_reindexed = df.reindex(dtindex, method='ffill')
    # return
    return df_reindexed


## import virtual currencies. import long format. save as matrices.

## def import function

def sql2df(folder, file):
    df_marketcap = sqlite3.connect(folder + file)
    df = pd.read_sql_query("SELECT * FROM coinmarketcap_coin", df_marketcap)
    df['date'] = df['cdate']
    del df['cdate']
    return df


def csv2df(folder, file):
    return pd.read_csv(folder + file, parse_dates=True)

## def clean df and export to matrices of interest

def df2matrices(df, start=None, end=None):
    # limit the nr of coins to speed up the computations
    # theoretically this is <=> to define market as "current top 200".
    max_nrcoins_indata = 200
    df = df.loc[df.ranknow < max_nrcoins_indata]

    # select cols
    df = df[['symbol', 'date', 'close', 'volume', 'market']]

    # make date column a date.
    df.date = pd.to_datetime(df.date)

    if start == None:
        start = dtindex[0]
    if end == None:
        end = dtindex[-1]

    # slice dates
    # df = df.loc[df.date >= start]
    # df = df.loc[df.date <= end]

    # create date time index object
    dtindex = pd.date_range(start, end, freq='D')
    # create price, volume, marketcap matrices by
    # selecting cols then pivoting and reindexing.
    price = df[['symbol', 'date',
                'close']].pivot_table(index='date', columns='symbol',
                                      values='close').reindex(index=dtindex)
    volume = df[['symbol', 'date',
                 'volume']].pivot_table(index='date', columns='symbol',
                                        values='volume').reindex(index=dtindex)
    marketcap = df[['symbol', 'date',
                    'market']].pivot_table(index='date', columns='symbol',
                                           values='market').reindex(index=dtindex)

    # check all three have same index
    assert (marketcap.index == price.index).all()
    assert (volume.index == price.index).all()

    return price, volume, marketcap


## import data. clean and export to matrices.
# sql2df(folder=FOLDER_3, file=FILE_1)
FOLDER_CSV = '/home/he2/Dropbox/Axlantic/data/other/raw/'
dfl_vcc_mat = csv2df(FOLDER_CSV, 'CryptoData.csv')
pri_vcc_mat, vol_vcc_mat, mca_vcc_mat = df2matrices(df=dfl_vcc_mat, start=START1, end=END1)

len(dfl_vcc_mat.symbol.unique())  # is 32 so HH is not done with database
dfl_vcc_mat.symbol.unique()

## create tkr

tkr_top200now = pri_vcc_mat.columns




## import traditional assets

# financial tickers
tkr_fin = ['Stocks', 'Bonds', 'Gold']

# background information on stocks bonds gold
name_bonds = "Vanguard Total Bond Market ETF"
url_bonds = "https://www.morningstar.com/etfs/ARCX/BND/quote.html"
name_stocks = "SP500"
url_stocks = "https://stooq.pl/q/?s=^spx"
name_gold = "Commodity Futures Price Quotes for Gold (COMEX)"
url_gold = "https://www.nasdaq.com/markets/gold.aspx"
# https://stooq.pl/q/?s=iau.us is another possibel choihce for gold

# choose start date = first day of vcc datetime index
START0 = pri_vcc_mat.index[0]
END0 = pri_vcc_mat.index[-1]

# download data either online or offline
online_download = False

if online_download:
    # download from stooql. example: https://stooq.pl/q/?s=^spx
    stocks = web.DataReader('^SPX', 'stooq', START0)
    bonds = web.DataReader('BND.US', 'stooq', START0)
    gold = web.DataReader('GC.F', 'stooq', START0)
    # concat price and volume matrix
    pri_fin_mat = pd.concat([stocks.Close, bonds.Close, gold.Close], axis=1)
    vol_fin_mat = pd.concat([stocks.Volume, bonds.Volume, gold.Volume], axis=1)
    # trim size
    pri_fin_mat = np.round(pri_fin_mat, 4)
    pri_fin_mat = pri_fin_mat[START0:]
    vol_fin_mat = vol_fin_mat[START0:]
    # rename
    pri_fin_mat.columns = tkr_fin
    vol_fin_mat.columns = tkr_fin
    # re index
    pri_fin_mat = re_index_date(pri_fin_mat)
    vol_fin_mat = re_index_date(vol_fin_mat)
    # save to csv
    pri_fin_mat.to_csv('object/pri_fin_mat.csv')
    vol_fin_mat.to_csv('object/vol_fin_mat.csv')

if not online_download:
    # read
    file_pri_fin = 'object/pri_fin_mat.csv'
    file_vol_fin = 'object/vol_fin_mat.csv'
    pri_fin_mat = pd.read_csv(file_pri_fin, index_col=0, parse_dates=True)
    vol_fin_mat = pd.read_csv(file_vol_fin , index_col=0, parse_dates=True)
    # re index
    pri_fin_mat = re_index_date(pri_fin_mat)
    vol_fin_mat = re_index_date(vol_fin_mat)
    # slice date
    pri_fin_mat = pri_fin_mat.loc[START0:END0]
    vol_fin_mat = vol_fin_mat.loc[START0:END0]

## create returns matrices

ret_vcc_mat = price2return(pri_vcc_mat, fill_na_0=True)
ret_fin_mat = price2return(pri_fin_mat, fill_na_0=True)

# Corr matrix will include the missing values
ret_vcc_mat_withna = price2return(pri_vcc_mat, fill_na_0=False)
ret_fin_mat_withna = price2return(pri_fin_mat, fill_na_0=False)
ret_fin_mat_withna.isnull().sum().sum()
ret_vcc_mat_withna[['BTC', 'ETH', 'XRP', 'LTC']].isnull().sum().sum()

