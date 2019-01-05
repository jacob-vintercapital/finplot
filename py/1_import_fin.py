'''
import traditional assets
'''

## create name for financial tickers

tkr_fin = ['Stocks', 'Bonds', 'Gold']

## background information on stocks bonds gold

name_bonds = "Vanguard Total Bond Market ETF"
url_bonds = "https://www.morningstar.com/etfs/ARCX/BND/quote.html"
name_stocks = "SP500"
url_stocks = "https://stooq.pl/q/?s=^spx"
name_gold = "Commodity Futures Price Quotes for Gold (COMEX)"
url_gold = "https://www.nasdaq.com/markets/gold.aspx"
# https://stooq.pl/q/?s=iau.us is another possibel choihce for gold

## choose start date = first day of vcc datetime index

START0 = pri_vcc_mat.index[0]
END0 = pri_vcc_mat.index[-1]















## --------------------------------------------------------------------------------------

## old method: download data either online or offline

ONLINE_DOWNLOAD = False

if ONLINE_DOWNLOAD:
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

if not ONLINE_DOWNLOAD:
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

## --------------------------------------------------------------------------------------

## new way of importing i think it is much better

sp500wei = pd.read_excel('notes2others/sp500weights.xlsx')
sp500wei = sp500wei[['Ticker', 'Weight']]
sp10 = sp500wei.nlargest(10, 'Weight')
tkr_sp10 = sp10.Ticker.tolist()
tkr_sp5 = tkr_sp10[0:5]
del sp10

# not tested. wrote on a plane.
# todo runt he code to test it

def ticker2pricevec(ticker, start, end, data_source='stooq'):
    price_vector = web.DataReader(name=ticker, data_source=data_source, 
                                  start=start, end=end)
    return price_vector['Close'] 


def tickerlist2pricemat(ticker_list, start, end, data_source='stooq', filepath=None):
    # put prices in a list 
    pri_sp10_list = []
    for tkr in tkr_sp10:
        price_vector = ticker2pricevec(tkr, start=start, end=end, 
                                       data_source=data_source)
        pri_sp10_list.append(price_vector)
    # put prices in a matrix 
    pri_sp10_mat = pd.concat(pri_sp10_list, axis=1)
    pri_sp10_mat.columns = tkr_sp10
    # re index 
    pri_sp10_mat = re_index_date(pri_sp10_mat)
    # save to csv 
    if filepath != None:
        pri_sp10_mat.to_csv(filepath)
    return pri_sp10_mat


FILEPATH_SP500 = 'object/pri_sp10_mat.csv'
FILEPATH_FIN =   'objcet/pri_fin_mat.csv'

if ONLINE_DOWNLOAD:
    pri_sp10_mat = tickerlist2pricemat(ticker_list=tkr_sp10,
                        start=START0, end=END0,
                        filepath=FILEPATH_SP500)
    pri_fin_mat = tickerlist2pricemat(ticker_list=['^SPX', 'BND.US', 'GC.F'],
                                      start=START0, end=END0,
                                      filepath=)
    pri_fin_mat.columns = tkr_fin
else:
    pri_sp10_mat = pd.read_csv(FILEPATH_SP500)
    pri_fin_mat = pd.read_csv(FILEPATH_FIN)


# end of new importing metohd

## --------------------------------------------------------------------------------------

