import yfinance as yf

with open('tickers.txt', 'r') as f:
    tickers = f.readlines()

tickers = [line.strip() for line in tickers]
good_tickers = []

for ticker in tickers:
    data = yf.download(ticker, start='2015-01-01', progress=False)
    if data.empty:
        continue
    else:
        good_tickers.append(ticker)

with open('clean_tickers.txt', 'w') as f:
    f.write('\n'.join(good_tickers))