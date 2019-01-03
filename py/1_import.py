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


## import virtual currencies

# choose to import either long or wide format.
# long is better for sql. wide works for sure.
import_long_format = True
import_wide_format = not import_long_format

if PC:
    filepath2 = 'input/CryptoData.csv'
else:
    filepath2 = '/home/he2/Dropbox/Axlantic/data/other/raw/CryptoData.csv'

if import_long_format:
    # read
    dfl_vcc = pd.read_csv(filepath2, parse_dates=True)
    dfl_vcc.info()
    # limit the nr of coins to speed up the computations
    # theoretically this is <=> define market as "current top 200".
    max_nrcoins_indata = 200
    dfl_vcc = dfl_vcc.loc[dfl_vcc.ranknow < max_nrcoins_indata]
    # select useful cols
    dfl_vcc = dfl_vcc[['symbol', 'date', 'close', 'volume', 'market']]
    dfl_vcc.head()
    # slice dates
    dfl_vcc = dfl_vcc.loc[dfl_vcc.date >= START1]
    # make date column a date. 
    assert len(dfl_vcc.date) == len(pd.to_datetime(dfl_vcc.date))
    dfl_vcc.date = pd.to_datetime(dfl_vcc.date)
    # create date time index object     
    dtindex = pd.date_range(min(dfl_vcc.date), 
                            max(dfl_vcc.date), 
                            freq='D')
    # create price, volume, marketcap matrices
    # select cols then pivot and reindex.
    pri_vcc_mat = dfl_vcc[['symbol', 'date',
                           'close']].pivot_table(index='date', columns='symbol',
                                          values='close').reindex(index=dtindex)
    vol_vcc_mat = dfl_vcc[['symbol', 'date',
                             'volume']].pivot_table(index='date', columns='symbol',
                                            values='volume').reindex(index=dtindex)
    mca_vcc_mat = dfl_vcc[['symbol', 'date',
                             'market']].pivot_table(index='date', columns='symbol',
                                            values='market').reindex(index=dtindex)

    # check all three have same index 
    assert (mca_vcc_mat.index == pri_vcc_mat.index).all()
    assert (vol_vcc_mat.index == pri_vcc_mat.index).all()

coins_top200 = pri_vcc_mat.columns

if import_wide_format:
    # read file
    filepath1 = 'input/CryptoDataWide.csv'
    df_vcc = pd.read_csv(filepath1, parse_dates=True)
    dfl_vcc = pd.read_csv(filepath2, parse_dates=True)
    # i get an error of mixed types. it is merely a warning however.
    # I tried using pd.read_csv("data.csv", dtype={"CallGuid": np.int64}) but it didnt work
    # index date
    df_vcc.set_index('date', inplace=True)
    df_vcc = re_index_date(df_vcc)
    # todo hakan, this is needed because pandas complained dates are not regular.
    # this led the .freq to not be daily which we need!
    # please double check the data you gave me so that this resampling does not render calculations incorrect.
    # create matrices: price, marketcap, volume
    pri_vcc_mat = df_vcc.filter(regex='^open.').fillna(0)
    mca_vcc_mat = df_vcc.filter(regex='^market.').fillna(0)
    vol_vcc_mat = df_vcc.filter(regex='^volume.').fillna(0)
    del df_vcc
    # rename
    tkr_vcc = [n.replace('open.', '') for n in pri_vcc_mat.columns]
    pri_vcc_mat.columns = tkr_vcc
    mca_vcc_mat.columns = tkr_vcc
    vol_vcc_mat.columns = tkr_vcc

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


(ret_vcc_mat == 0).mean().mean()

# create new datetime index, of finance dates (weekdays)
# dtindex_fin = pri_fin_mat.index
