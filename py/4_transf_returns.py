'''
have imported price matrices. convert them to return matrices.
'''


## create ret mat

ret_vcc_mat = price2return(pri_vcc_mat, fill_na_0=True)
ret_fin_mat = price2return(pri_fin_mat, fill_na_0=True)

## create ret mat with NA included (needed for corr matrices)

ret_vcc_mat_withna = price2return(pri_vcc_mat, fill_na_0=False)
ret_fin_mat_withna = price2return(pri_fin_mat, fill_na_0=False)

# check
ret_fin_mat_withna.isnull().sum().sum()
ret_vcc_mat_withna[['BTC', 'ETH', 'XRP', 'LTC']].isnull().sum().sum()


