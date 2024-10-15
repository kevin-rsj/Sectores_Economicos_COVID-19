import yfinance as yf
import pandas as pd

# Tickers organizado por sectorers
tickers = {
     'Supermercados': ['WMT', 'COST', 'KR'],
    'Farmaceutica': ['PFE', 'JNJ', 'MRK'],
    'Tecnologia de Comunicacion': ['ZM', 'MSFT', 'CSCO'],
    'E-commerce': ['AMZN', 'BABA', 'EBAY'],
    'Telecomunicaciones': ['VZ', 'T', 'TMUS'],
    'Finanzas': ['JPM', 'BAC', 'GS'],
    'Energia': ['XOM', 'CVX', 'BP'],
    'Manufactura': ['GM', 'CAT', 'F']
}

# Descarga data desde Yahoo Finance para todos tickers
raw_data = pd.DataFrame()

for sector, ticker_list in tickers.items():
    for ticker in ticker_list:
        data = yf.download(ticker, start="2019-06-01", end="2022-6-30")
        data['Sector'] = sector
        data['Ticker'] = ticker
        raw_data = pd.concat([raw_data, data])

# Grabar datos en archivo CSV 
raw_data.to_csv('raw_data.csv')
print("Data downloaded and saved to 'raw_data.csv'")