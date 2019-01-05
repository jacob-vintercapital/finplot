"""
output: interesting plots to /output/ and /output/vip/

here some objects are created, especially in the rollcor part.

not to self:
For inspiration see filestr.md
All plots here are done with a certain startdate
See html for details of inspiration. below is what i 25th of july thought was most needed.
"""

## ticker and selections

# create new ticker vectors
tkr_sel = ['BTC', 'ETH']
tkr_fin = ['Stocks', 'Bonds'] #not gold
tkr_sel_blx = tkr_sel + ['BLX']
tkr_sel_blx_fin = tkr_sel_blx + tkr_fin
tkr_t10now_blx = tkr_t10now + ['BLX']
tkr_fin_blx = tkr_fin + ['BLX']

# create color list           
# http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
#clr_btc = 'xkcd:greyish blue'
#clr_eth = 'xkcd:slate'
#clr_oth = 'xkcd:deep sea blue'
#clr_blx = 'xkcd:sky blue'
clr_btc = '#0000cd'
clr_eth = '#006400'
clr_oth = '#2f4f4f'
clr_blx = '#483d8b'
alpha_ = 0.80
clr_sel = [clr_btc, clr_eth]
clr_sel_blx = [clr_btc, clr_eth, clr_blx]




## prices: $100 investment a year ago 


# start a year ago
ret_vcc_mat.index[-1] - DateOffset(years=1)
START2 = START1
END2 = END1
pri_vcc_mat_2 = return2aum(ret_vcc_mat.loc[START2:, tkr_t5now])
pri_vcc_mat_2.plot(logy=True)
plt.title('$100 investment a year ago')
plt.ylabel('Indexed price \n(start at $100)')
plt.savefig('output/vcc/ret/price-fund_vs_coins.png')
if save_large_png == True:
    plt.savefig('output/vcc/ret/price-fund_vs_coins_largesize.png', dpi=750)

## returns and sharpe, depending on startdate

retvol(ret_vcc_mat[tkr_t10now])
sharpe(ret_vcc_mat[tkr_t10now], showall=True)

# vary the start date
plot_many_sharpe = False
if plot_many_sharpe:
  startlist = ['2015', '2016', '2017', '2016-04', '2017-04']
  for s in startlist:
    sharpe(ret_vcc_mat.loc[s:, tkr_t10now], showall=True).plot.barh()
    plt.title("start @" + s)
    plt.show()


## correlation matrices

# create tickers corr plots
tkr_cor1 = tkr_t10now.tolist() + tkr_fin + [r1.name]
tkr_cor2 = tkr_fin + tkr_t5now.tolist() + [r1.name] # looks assymetric but is correct

# create ret mat for corr plots
ret_cor1_mat = ret_fin_mat_withna.\
  join(ret_vcc_mat_withna[tkr_t10now], how='inner').\
  join(r1, how='inner')
assert (ret_cor1_mat.index == r1.index).all()

# create ret mat: fill na with column mean
ret_cor1_mat_namean = ret_cor1_mat.fillna(ret_cor1_mat.mean())

# create ret mat: go from daily to monthly returns
ret_cor1_mat_mthly = ret_cor1_mat.resample('MS').sum()
ret_cor1_mat_namean_mthly = ret_cor1_mat_namean.resample('MS').sum()

# plots
if CLINUX:
  plt.style.available
  with plt.style.context('seaborn-white'):

    # first plot tkr_cor1

    # 1
    show_corr_plot(df=ret_cor1_mat)
    plt.savefig('output/vcc/ret/cor-1.png')
    plt.close()

    # 1 with fillna column mean
    show_corr_plot(df=ret_cor1_mat_namean)
    plt.savefig('output/vcc/ret/cor-1-namean.png')
    plt.close()

    # 1 monthly
    title1m = 'Correlation matrix \n Monthly data'
    show_corr_plot(df=ret_cor1_mat_mthly, title=title1m)
    plt.savefig('output/vcc/ret/cor-1-mthly.png')
    plt.close()

    # then plot tkr_cor2

    # 2
    show_corr_plot(df=ret_cor1_mat[tkr_cor2])
    plt.savefig('output/vcc/ret/cor-2.png')
    plt.close()

    # 2 with fillna column mean
    show_corr_plot(df=ret_cor1_mat_namean[tkr_cor2])
    plt.savefig('output/vcc/ret/cor-2-namean.png')
    plt.close()


    # top 10 vcc
    show_corr_plot(df=ret_cor1_mat_namean[tkr_t10now])
    plt.savefig('output/vcc/ret/cor-t10now-namean.png')
    plt.close()

    # top 5 vcc
    show_corr_plot(df=ret_cor1_mat_namean[tkr_t5now])
    plt.savefig('output/vcc/ret/cor-t5now-namean.png')
    plt.close()




## plot correlation over time

# create matrix
#ret_t10_mat = ret_vcc_mat[tkr_t10now]

# create roll corr objet
cor_cor1_mat = ret_cor1_mat.rolling(365).\
  corr(ret_t10_mat.BTC).\
  drop('BTC', axis=1)
tkr_t10woBTC = tkr_t10now[1:]
tkr_t5woBTC = tkr_t5now[1:]


# corr over time top 10
cor_cor1_mat[tkr_t10woBTC].rolling(20).mean().plot()
plt.ylabel('Correlation vs BTC')
#plt.gca().set_ylim(top=1.01)
plt.title('Rolling 1y correlation \n All vs BTC')
plt.savefig('output/vcc/ret/cor-roll-t10_smooth20.png')
plt.close()

# top 5
cor_cor1_mat[tkr_t5woBTC].rolling(20).mean().plot()
plt.ylabel('Correlation vs BTC')
plt.title('Rolling 1y correlation \n All vs BTC')
plt.savefig('output/vcc/ret/cor-roll-t5_smooth20.png')
plt.close()

# top 5 + r1

#cor_cor1_mat[tkr_t5woBTC.tolist() + ['t10-wm-rm']].rolling(20).mean().plot()
cor_cor1_mat[tkr_t5woBTC].rolling(20).mean().plot()
cor_cor1_mat['t10-wm-rm'].rolling(20).mean().plot(color='black', linewidth=1.5)
plt.legend()
plt.ylabel('Correlation vs BTC')
plt.title('Rolling 1y correlation \n All vs BTC')
plt.savefig('output/vcc/ret/cor-roll-t5-bl10_smooth20.png')
plt.close()


## woobull

"""
do like this one https://woobull.com/data-visualisation-alt-coins-that-achieved-5m-market-cap-vs-bitcoin/
https://woobull.com/data-visualisation-118-coins-plotted-over-time-this-is-why-hodl-alt-coin-indexes-dont-work/

take tkr_beeninblx, the coins that has been in the fund once. graph their price.
adjust the color of the line so that it is more transparent when it is not in the fund,
this information is inside b_mat. would be a nice graph. below is some proxy code:
"""

return2aum(ret_vcc_mat.loc['2016':, tkr_t10hasbeen]).\
  plot(logy=True, legend=False, alpha=0.5)
plt.title('$100 Investment')
plt.ylabel('USD value after $100 investment \n on the day it first appears on coinmarketcap.com')
plt.savefig('output/vcc/ret/woobull.png')
# todo: now edit the transpancy, see url:
# https://stackoverflow.com/questions/51841146/time-series-plot-of-assets-change-transparency-based-on-another-matrix

## corr matrices for part i and part ii in whitepaper

# example of ticker lists to use
tkr_t5hist
tkr_t10hist
tkr_sp10
tkr_sp5
tkr_fin
['Stocks', 'Bonds', 'Gold']
['SP500', 'Bonds', 'Gold']

# create a ret mat with all tickers of interest available
tkr_cor3 = tkr_t10hist + tkr_sp10 + ['BL10'] + ['SP500', 'Bonds']
ret_cor3_mat = pd.concat([ret_vcc_mat[tkr_t10hist],
                          ret_sp10_mat,
                          r1,
                          ret_fin_mat[['Stocks', 'Bonds']] # or 'SP500' not sure with naming now...
                          ], axis=1)
ret_cor3_mat.columns = tkr_cor3
# iff pd.concat does not work try .join how='inner'
#ret_cor3_mat = ret_vcc_mat[tkr_t10hist].join( sp10 ).join( bl10 ).join( sp500 )

# create new cols for TRD and BAL
ret_cor3_mat['TRD'] = 0.60 * ret_cor3_mat['SP500'] + 0.40 * ret_cor3_mat['Bonds']
ret_cor3_mat['BAL'] = 0.95 * ret_cor3_mat['TRD'] + 0.05 * ret_cor3_mat['BL10']
tkr_cor3 = tkr_cor3 + ['TRD', 'BAL']

# plot all that are of interest, select which ones later
plt.close('all')
# part i
show_corr_plot(df=ret_cor3_mat, cols=tkr_t5hist)
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_t10hist)
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_t5hist + ['BL10'])
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_sp5)
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_sp10)
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_sp10 + ['SP500'])
plt.show()
# part ii
show_corr_plot(df=ret_cor3_mat, cols=tkr_t5hist + tkr_sp5 + ['BL10'] + ['SP500'])
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_t10hist + tkr_sp10 + ['BL10'] + ['SP500'])
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=tkr_t5hist[0:3] + tkr_sp5[0:3] + ['BL10'] + ['SP500'])
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=)
plt.show()
show_corr_plot(df=ret_cor3_mat, cols=)
plt.show()
# when done watching them: close all windows
plt.close('all')