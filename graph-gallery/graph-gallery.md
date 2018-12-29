---
title: Graph Gallery
description: Contain the important graphs, arranged by topic and incl. comments/explanations
created: 2018-12-19
author: Vinter Capital

documentclass: article # article report book memoir
fontsize: 12
linestretch: 1.25
fontfamily: mathpazo

toc: true
toc-depth: 2
toc-title:
numbersections: true

lof: false # list of figures with caption
pagestyle: empty # plain empty headings

include-before-body: disclaimer.md

columns: 1
wrap: preserve
dpi: 96 # default 96

default-image-extension: png
---

    \graphicspath{{./Figures/}}



# test

caption in many pages



# TODO

make a python script that send to terminal, firstly .md to .tex secondly .tex to .pdf

this section describes what i need to do.

there are errors in the files. you cannot point to /jl/Documents/crinfu/output because some are wrong e.g. turnover_1 is not at all what it should be.
solve this by running code in pycharm on clinux to get the correct output.

# Theory

For those accustomed to time series analysis and reading financial charts, this section is not needed. For everyone else, this section provides a point of reference - similar to a glossary.

## Prices

## Returns

## Weights

## Volatility

## Correlation

## Autocorrelation

## Rolling windowkeyboard

todo insert plot from my su thesis

If you have data from day 1 to day 1000, you can split it up into rolling time period of 100 days so that the first windows is day 1 to 100, the second window is day 2 to 101, and so on.

Using these windows, each of which contain 100 days, we can then compute a statistic such as the mean price for each window. By plotting the mean price on the y-axis and the window's end date on the x-axis, we can see how the mean changed depending on the data that is used.

Another feature of rolling windows is to smooth data that is volatile, so that the lines in a graph are smoother.


## Weight caps and floors

With a cap, the weight of asset get modified from `w'` to
`w = max(w', weight cap)`.
With a weight floor, the weight of asset get modified from `w'` to
`w = min(w', weight floor)`.

A weight cap can reduce the weight in large assets, and a weight floors can increase the weight in small assets. Large and small, in tis contect, refer to the market capitalization of the asset.

When a weight cap is imposed, the "removed" weights must be redistributed so that the weights sum to 100%. For example, if BTC has weight 55% according to its market capitalization, and a basket has a weight cap of 30%, then 25% weight is removed from the basked and that must be redistributed to other assets somehow.
Vinter Capital achieve this by taking the removed weight (e.g. 25%) and allocating it to all other assets in the basket, according to their previous weight.

The assets whose weights change when a weight floor is imposed get an increased weight.  When a weight floor is imposed, the "added" weights must be taken from somewhere so that the weights sum to 100%. For example, if the tenth asset has a market capitalization so that its weight is 0.6% and we impose a weight floor of 1% then the extra 0.4% has to come from somewhere - otherwise the index weights sum to 100.4%.
Vinter Capital achieve this by stealing the added weight (e.g. 0.4%) from all other assets in the basket, except those who have been affected from the cap.


# Files

```
/home/he2/Documents/crinfu/output/vcc/vol/volfr_vcc_bsk1_smooth20.png
/home/he2/Documents/crinfu/output/vcc/vol/volfr_vcc_smooth20.png
/home/he2/Documents/crinfu/output/vcc/vol/vol_vcc_bsk1_smooth20.png
/home/he2/Documents/crinfu/output/vcc/vol/vol_vcc_smooth20.png

/home/he2/Documents/crinfu/output/vcc/ret/price-fund_vs_coins.png
/home/he2/Documents/crinfu/output/vcc/ret/pri_portfolios.png
/home/he2/Documents/crinfu/output/vcc/ret/pri_portfolios_2.png
/home/he2/Documents/crinfu/output/vcc/ret/pri_t5.png
/home/he2/Documents/crinfu/output/vcc/ret/pri_tkr3_market.png
/home/he2/Documents/crinfu/output/vcc/ret/retvol_scatter_text.png
/home/he2/Documents/crinfu/output/vcc/ret/total_marketcap.png
/home/he2/Documents/crinfu/output/vcc/ret/vcc-rollcorr-t5_smooth20.png
/home/he2/Documents/crinfu/output/vcc/ret/vcc-rollcorr-t10_smooth20.png
/home/he2/Documents/crinfu/output/vcc/ret/woobull.png
/home/he2/Documents/crinfu/output/vcc/ret/pri_portfolios.csv

/home/he2/Documents/crinfu/output/vcc/mca/mca_vcc.png
/home/he2/Documents/crinfu/output/vcc/mca/mca_vcc_bsk1.png

/home/he2/Documents/crinfu/output/bsk/wei/capsweight floors_effect_1_alts.png
/home/he2/Documents/crinfu/output/bsk/wei/capsweight floors_effect_1_BTC.png
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches1.png
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches1minus4.png
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches4.png
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches8.png
/home/he2/Documents/crinfu/output/bsk/wei/mcafr_bsk1bsk4_smooth20.png
/home/he2/Documents/crinfu/output/bsk/wei/smoothing_w1.png
/home/he2/Documents/crinfu/output/bsk/wei/turnover_1.png
/home/he2/Documents/crinfu/output/bsk/wei/turnover_2.png
/home/he2/Documents/crinfu/output/bsk/wei/volume_5vs10_1.png
/home/he2/Documents/crinfu/output/bsk/wei/w1_alts.png
/home/he2/Documents/crinfu/output/bsk/wei/w1_area.png
/home/he2/Documents/crinfu/output/bsk/wei/w4-1m_alts.png
/home/he2/Documents/crinfu/output/bsk/wei/w4_alts.png
/home/he2/Documents/crinfu/output/bsk/wei/w4_area.png
/home/he2/Documents/crinfu/output/bsk/wei/w4-w1_area.png
/home/he2/Documents/crinfu/output/bsk/wei/wd1_tkr_insouts_mostwei.png
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches_bsk1.txt
/home/he2/Documents/crinfu/output/bsk/wei/coinswitches_bsk1_minus_bsk4.txt
/home/he2/Documents/crinfu/output/bsk/wei/member_sum_wei_t5-wm-rm.txt
/home/he2/Documents/crinfu/output/bsk/wei/member_sum_wei_t10-wm-rm.txt
/home/he2/Documents/crinfu/output/bsk/wei/nrof_coinsw_w1.csv
/home/he2/Documents/crinfu/output/bsk/wei/smoothing_1.csv
/home/he2/Documents/crinfu/output/bsk/wei/tkr_insouts_mostwei_sum.csv
/home/he2/Documents/crinfu/output/bsk/wei/w4_minusw_1m_mean.csv
/home/he2/Documents/crinfu/output/bsk/wei/wd_mean.txt
/home/he2/Documents/crinfu/output/bsk/wei/wei_mthly_t5-wm-rm.csv
/home/he2/Documents/crinfu/output/bsk/wei/wei_mthly_t10-wm-rm.csv
/home/he2/Documents/crinfu/output/bsk/wei/w smooth minus w raw, abs(mean()).csv

/home/he2/Documents/crinfu/output/bsk/ret/ACF_bsk1.png
/home/he2/Documents/crinfu/output/bsk/ret/ACF_btc.png
/home/he2/Documents/crinfu/output/bsk/ret/bsk-rollcorr-1.png
/home/he2/Documents/crinfu/output/bsk/ret/contribution_bsk1.png
/home/he2/Documents/crinfu/output/bsk/ret/contribution_bsk4.png
/home/he2/Documents/crinfu/output/bsk/ret/qqplot_BTC.png
/home/he2/Documents/crinfu/output/bsk/ret/qqplot_market.png
/home/he2/Documents/crinfu/output/bsk/ret/ret_dens_market.png
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_box.png
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_rollbeta.png
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_rolling_sharpe_1.png
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_rollvol.png
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_beta.csv
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_descr_interval.csv
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_risk.csv
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_yearly_mean.csv
/home/he2/Documents/crinfu/output/bsk/ret/retmat1_yearly_vol.csv
```


# Description of digital assets

## Prices

pri_t5

## Market cap

total_marketcap

## Returns

qqplot_market
qqplot_BTC


# Description and comparison of indices

## Prices

## Market cap

## Returns

contribution_bsk1
contribution_bsk4

retmat1_box

## Risk & returns

retvol_scatter_text


## Risk & return

retmat1_rollvol

retmat1_rolling_sharpe_1

retmat1_rollbeta

## Weights

### caps and floors

> Question: How does the weight in each asset change when weight caps and floors are imposed?

The answer is given by the stacked area chart of weight difference between on one hand a regular market capitalization weighted top 10 basket, versus on the other hand imposing weight caps and floors.
(The defintion for caps and floors are found in the theory section.)

![Stacked area chart: Effect of including caps and floors.](/home/he2/Documents/crinfu/output/bsk/wei/capsfloors_effect_1_alts.png)

On the y-axis we see how large this effect is. The colors represent an asset - clearly ETH is most affected, followed by XRP and LTC. The reason for this is the historical dominance of BTC well above 50%. With a cap of 50% some weight is taken from BTC and allocated to the other nine assets, in accordance with their previous weight. With a floor of 2% the smallest assets get a boost in their weight, especially the ninth and tenth asset. In relative terms, changes can be vast (it can go from 0.2% to 2% which is a 10x increase) but in absolute terms the changes are small and are thus not seen clearly in this graph.

A lower cap value, e.g. 30% instead of 50%,   decrease the weight in BTC even more - this in turn increases t the weight in alt coins since the weights must sum to one.

### some files

w1_alts.png
w4_alts.png

w4-1m_alts.png
w1_area.png

### fraction of market cap

This graph answer the question:

> How much closer to the "total" market is a top 10 compared to a top 5 basket?

The fraction of total market capitalzation for a certain basket is defined as the market capitalzation of the assets in the basket, divided by the total market capitalzation. (To get smoother lines a 20 day mean is imposed in the graph.) In order to be logically consistent and practical, we define the total market as a basket with 200 assets weighted by market capitalzation.

![A top 10 basket capture around 90% of the total market capitalization, and a top 5 basket slightly less.     Over time, the fraction is decreasing, indicating that the coins with a market capitalzation ranked below 11 are growing in size relative to the top 10. In the future, a top 20 or top 50 index might be needed to capture the market.](/home/he2/Documents/crinfu/output/bsk/wei/mcafr_bsk1bsk4_smooth20.png)


> stylish question: is it better to put everything in the caption, or is it better to

### Turnover on rebalancing date



> What is the turnover in small assets?

![this fig is incorrect. see todo section.](/home/he2/Documents/crinfu/output/bsk/wei/turnover_1.png)

## Correlation matrix

## Rolling correlation

The correlation matrix looks different depending on which time period we use. To mitigate this weakness, they can be accompanied by graphing the correlation using a rolling window.

## Autocorrelation

ACF_bsk1
ACF_btc

## Effect of caps and weight floors

capsweight floors_effect_1_alts


## Effect of smoothing

Close to none.
