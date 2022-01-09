# trading
1. First of all, I picked up only USD denominated crypto-currencies with "create_a_list_of_all_files.py". Output file is "usd-list.csv".

2. I created a summary of trading activities of the crypto-currencies in "usd-list.csv" with "create_a_summary_from_a_list2.py". Then I sorted by the trading volume. Output file is "usd-Summary3.csv".

3. I picked up top 20 liquid crypto-currencies, "top20usd.csv". I calculated daily returns of 20 currencies with "calc-returns.py". Output file is "returns.csv".

4. I calculated correlations between the 20 currencies excluding the last 1 year data with "correlations.py". Output file is "correlations.csv". All pairs show fairly high correlation coefficients, about 0.6.

5. As crypto-currencies are highly correlated each other, I assume smaller currencies follow the direction btcusd is heading to because it is the most liquid currency. When btcusd goes up/down more than threshold 1 and another currency goes up/down less than threshould 2, we initiate a long/short position. We liquidate this position in the next 1 minute interval. In order to avoid overfitting, I did backtesting with data between 2 years ago and 1 year ago and determine the parameters with "trend_follower.py". I apply the parameters for last 1 year data. Result was "btcusd-ethusdtrend_follow2Y.csv". According to the backtesting results, thereshould 1 - 40 bps and threshould 2 - 10 bps look good.
