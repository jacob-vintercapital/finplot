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

