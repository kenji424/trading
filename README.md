# trading
1. First of all, I picked up only USD denominated crypto-currencies with "create_a_list_of_all_files.py". Output file is "usd-list.csv".

2. I created a summary of trading activities of the crypto-currencies in "usd-list.csv" with "create_a_summary_from_a_list2.py". Then I sorted by the trading volume. Output file is "usd-Summary3.csv".

3. I picked up top 20 liquid crypto-currencies, "top20usd.csv". I calculated daily returns of 20 currencies with "calc-returns.py". Output file is "returns.csv".

4. I calculated correlations between the 20 currencies excluding the last 1 year data with "correlations.py". Output file is "correlations.csv". All pairs show fairly high correlation coefficients, about 0.6.

5. As crypto-currencies are highly correlated with each other, I assume smaller currencies follow the direction btcusd is heading to because it is the most liquid currency. When btcusd goes up/down more than threshold 1 and another currency goes up/down less than threshould 2, we initiate a long/short position. We liquidate this position in the next 1 minute interval. In order to avoid overfitting, I did backtesting with data between 2 years ago and 1 year ago and determine the parameters with "trend_follower.py", and then I apply the parameters for the last 1 year data. Result was "btcusd-ethusdtrend_follow2Y.csv". According to the backtesting results, thereshould 1 - 30 bps and threshould 2 - 20 bps look good. When I applied the same parameters for the last 1 year data, results were "btcusd-ethusdtrend_follow1Y.csv". Commissions are not included in this calculation.

6. I did the same calculation on other currencies and created a summary, "trend_follow_summary.ods". The same parameters looked good on the other currencies as well. As a conclusion, we can say other smaller currencies are also following btcusd.

7. I did back testing on trend follower strategy with a longer holding period. This time I skipped the trading opportunities in the next 1 minute trading opportunities and held positions more than 1 minute. Results are "trend_follow_summary2.ods". I didn't see a clear tendency that the longer holding period is better in this strategy.
