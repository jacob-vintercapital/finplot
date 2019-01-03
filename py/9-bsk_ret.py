"""
create a bunch of different indexes using ggindex() and compare their properties.
"""

plt.close('all')
plt.clf()


# set start end date
ret_bsk_mat.index[0]
ret_bsk_mat.index[-1]

# corr
ret_bsk_mat.corr().round(4)
ret_bsk_mat.corr().round(4).to_csv('output/bsk/ret/corr_1.csv')

# todo add corr plot


# sharpe sortino
sharpe_1 = sharpe(ret_bsk_mat, showall=True).round(2)
sortino_1 = sortino(ret_bsk_mat).round(2)
sortino_1.name = 'Sortino'
sharpe_1 = pd.concat([sharpe_1, sortino_1], axis=1)
sharpe_1.to_csv('output/bsk/ret/sharpe_1.csv')
sharpe_1

# price
return2aum(ret_bsk_mat).plot(logy=True)
plt.title('$100 Investment')
plt.ylabel('Value')
plt.savefig('output/bsk/ret/pri_bsk_a.png')
plt.close(); plt.clf()

# corr over time
cor90_bsk_mat = ret_bsk_mat.rolling(365).corr(ret_bsk_mat[r1.name])
cor90_bsk_mat = cor90_bsk_mat.drop(r1.name, axis=1)
cor90_bsk_mat.plot()
plt.ylabel('Correlation vs t10-wm-rm')
plt.gca().set_ylim(top=1.01)
plt.title('Rolling 1y correlation \n All vs t10-wm-rm')
plt.savefig('output/bsk/ret/bsk-rollcorr-1.png')
plt.close(); plt.clf()

# choose a few baskets
retmat1 = pd.concat([r0, r1, r2, r3, r8,
                     ret_vcc_mat.loc[r1.index[0]:, 'BTC']
                     ], axis=1)
retmat1.isnull().sum()

# describe. how does ithandla na?
retmat1.describe()

# volatility over time
retmat1.rolling(90).std().rolling(10).mean().plot()
plt.title('Rolling 90 days volatility')
plt.ylabel('Volatility \n (Smoothed with 10 day mean)')
plt.savefig('output/bsk/ret/retmat1_rollvol.png')
plt.close(); plt.clf()
# same but smoothed

# mean vola, with upper and lower limits
tbl2 = pd.concat([retmat1.std() - 2*retmat1.std().std(),
                  retmat1.std(),
                  retmat1.std() + 2*retmat1.std().std()],
                 axis=1)
tbl2 = tbl2 * np.sqrt(365)
tbl2.columns = ['lower', 'mean volatility', 'upper']
tbl2.round(3)

# returns interval
returns_interval(retmat1)
returns_interval(retmat1).to_csv('output/bsk/ret/retmat1_descr_interval.csv')

# sharpe
sharpe(retmat1, showall=True)

ret_bsk_mat.columns
ret_bsk_mat.columns[-1+3]

# info ratio
information_ratio(retmat1, benchmark='market')

# risk return
pd.concat([sharpe(retmat1, showall=True),
           information_ratio(retmat1, benchmark='market'),
           tracking_error(retmat1, benchmark='market')],
          axis=1).T.round(2).\
  to_csv('output/bsk/ret/retmat1_risk.csv')

# ret and vol by year
retmat1_yearly_mean = (retmat1.groupby(retmat1.index.year)).mean().round(2)*365
retmat1_yearly_mean.to_csv('output/bsk/ret/retmat1_yearly_mean.csv')
retmat1_yearly_vol = (retmat1.groupby(retmat1.index.year)).std().round(2)*np.sqrt(365)
retmat1_yearly_vol.to_csv('output/bsk/ret/retmat1_yearly_vol.csv')


# rolling sharpe
retmat1.rolling(365).apply(sharpe).rolling(30).mean().plot()
plt.title('Sharpe ratio rolling 1y')
plt.ylabel('Sharpe ratio \n (Smoothed with 30d mean)')
plt.savefig('output/bsk/ret/retmat1_rolling_sharpe_1.png')
plt.close(); plt.clf()

# beta
beta(retmat1).round(3).to_csv('output/bsk/ret/retmat1_beta.csv')

# rolling beta

# def custom function because we cannot do like above with .apply(sharpe)
def roll(df, w):
  # stack df.values w-times shifted once at each stack
  roll_array = np.dstack([df.values[i:i + w, :] for i in range(len(df.index) - w + 1)]).T
  # roll_array is now a 3-D array and can be read into
  # a pandas panel object
  panel = pd.Panel(roll_array,
                   items=df.index[w - 1:],
                   major_axis=df.columns,
                   minor_axis=pd.Index(range(w), name='roll'))
  # convert to dataframe and pivot + groupby
  # is now ready for any action normally performed
  # on a groupby object
  return panel.to_frame().unstack().T.groupby(level=0)
# todo change from Panel() to another method.
# Panel is deprecated and will be removed in a future version.
# The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
# Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
# Pandas provides a `.to_xarray()` method to help automate this conversion.

# see rolling beta
roll(retmat1, w=90).apply(beta).rolling(10).mean().plot()
plt.title('Rolling 90 days beta')
plt.ylabel('Beta \n (Smoothed with 10 day mean)')
plt.savefig('output/bsk/ret/retmat1_rollbeta.png')
plt.close(); plt.clf()

## ret top 10

# this should be placed in another file! todo

ret_vcc_mat[tkr_t10now]

## ret distribution

retmat1.max()
retmat1.min()
retmat1.describe()

# box
titlebox = 'Distribution of daily returns'
retmat1.plot.box()
plt.ylabel('Daily returns')
plt.title(titlebox)
plt.savefig('output/bsk/ret/retmat1_box.png')
plt.close()

# violin
if CLINUX:
    long_retmat1 = retmat1.melt()
    long_retmat1.columns = ['symbol', 'return']
    sns.violinplot(x='return', y='symbol', data=long_retmat1)
    plt.title(titlebox)
    plt.savefig('output/bsk/ret/retmat1_violin.png')
    plt.close(); plt.clf()

# density
if CLINUX:
    retmat1.columns
    sns.kdeplot(retmat1['BTC'], cumulative=True)
    sns.kdeplot(retmat1['market'], cumulative=True)
    sns.kdeplot(retmat1['t10-wm-rm'], cumulative=True)
    plt.title(titlebox + ' CDF plot')
    plt.savefig('output/bsk/ret/retmat1_cdf.png')
    plt.close(); plt.clf()

# hist
retmat1.columns
retmat1[retmat1.columns[1]].plot.hist()
plt.title(retmat1.columns[1])
plt.close(); plt.clf()

dens = sm.nonparametric.KDEUnivariate(retmat1.market)
dens.fit()
plt.plot(dens.cdf)
plt.savefig('output/bsk/ret/ret_dens_market.png')
plt.close('all'); plt.clf()

# todo not at all like in thesis vid t distr df=4

def qqplot(ret_vec, name=''):
  sm.qqplot(ret_vec, stats.t, fit=True, line='45')
  #sm.qqplot(retmat1.market, stats.t, distargs=(3,))
  plt.title('Q-Q-plot ' + name)
  filename = 'output/bsk/ret/q-q-plot_' + name + '.png'
  plt.savefig(filename)
  plt.title('Q-Q Plot market')
  plt.close(); plt.clf()
qqplot(retmat1.BTC, 'BTC')
qqplot(retmat1.market, 'market')
# todo read up on statsmodel regarding the params used.

# value at risk
retmat1.quantile(0.05).round(3)

# skew and kurt (3rd 4th moment)
retmat1.skew()
retmat1.kurt()

## contribution

# given a date, what is the contrubtion of each asset in the basket?
contr1 = w1 * ret_vcc_mat * 365
contr4 = w4 * ret_vcc_mat * 365
contr1.mean().nlargest(5)
contr1.mean().nsmallest(5)
tkr_temp1 = contr1.mean().nlargest(5).index.tolist()
tkr_temp2 = contr1.mean().nsmallest(5).index.tolist()
#tkr_most_contrib = tkr_temp1.union(tkr_temp2)
tkr_most_contrib = tkr_temp1 + tkr_temp2

# plot
contr1[tkr_most_contrib].mean().plot.barh()
plt.show()

# plot
contr1[tkr_t10now].mean().plot.barh()
plt.title('Mean contribution \n in ' + r1.name)
plt.xlabel('Contribution = weight times annualized return')
plt.ylabel('Current top 10 assets')
plt.savefig('output/bsk/ret/contribution_bsk1.png')
plt.close(); plt.clf()

# plot
tkr_t5now
contr4[tkr_t5now].mean().plot.barh()
plt.title('Mean contribution \n in ' + r4.name)
plt.xlabel('Contribution = weight times annualized return')
plt.ylabel('Current top 5 assets')
plt.savefig('output/bsk/ret/contribution_bsk4.png')
plt.close(); plt.clf()

## density of ret

pairs_plot = False # turning on takes time to compute and the file is already saved
if pairs_plot:
    g = sns.PairGrid(retmat1)
    g = g.map_upper(plt.scatter)
    g = g.map_lower(sns.kdeplot, cmap="Blues_d")
    g = g.map_diag(sns.kdeplot, lw=3, legend=False)
    plt.show()

##