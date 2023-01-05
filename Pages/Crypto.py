import streamlit as st
import requests
import cryptowatch as cw

# Set your API Key, it is by default read from  your ~/.cw/credentials.yml file
cw.api_key = "2Q1K00N1JB9EHW5JNGGY"

# Assets
cw.assets.list()
cw.assets.get("BTC")

# Exchanges
cw.exchanges.list()
cw.exchanges.get("KRAKEN")

# Instruments
cw.instruments.list()
cw.instruments.get("BTCUSD")

# Markets
cw.markets.list() # Returns list of all markets on all exchanges
cw.markets.list("BINANCE") # Returns all markets on Binance

# Returns market summary (last, high, low, change, volume)
cw.markets.get("KRAKEN:BTCUSD")
# Return market candlestick info (open, high, low, close, volume) on some timeframes
cw.markets.get("KRAKEN:BTCUSD", ohlc=True, periods=["4h", "1h", "1d"])

# Returns market last trades
cw.markets.get("KRAKEN:BTCUSD", trades=True)

# Return market current orderbook
cw.markets.get("KRAKEN:BTCUSD", orderbook=True)
# Return market current orderbook liquidity
cw.markets.get("KRAKEN:BTCUSD", liquidity=True)

import cryptowatch as cw

# Set your API Key
cw.api_key = "2Q1K00N1JB9EHW5JNGGY"

# Subscribe to resources (https://docs.cryptowat.ch/websocket-api/data-subscriptions#resources)
cw.stream.subscriptions = ["markets:*:trades"]

# What to do on each trade update
def handle_trades_update(trade_update):
    """
        trade_update follows Cryptowatch protocol buffer format:
        https://github.com/cryptowatch/proto/blob/master/public/markets/market.proto
    """
    market_msg = ">>> Market#{} Exchange#{} Pair#{}: {} New Trades".format(
        trade_update.marketUpdate.market.marketId,
        trade_update.marketUpdate.market.exchangeId,
        trade_update.marketUpdate.market.currencyPairId,
        len(trade_update.marketUpdate.tradesUpdate.trades),
    )
    print(market_msg)
    for trade in trade_update.marketUpdate.tradesUpdate.trades:
        trade_msg = "\tID:{} TIMESTAMP:{} TIMESTAMPNANO:{} PRICE:{} AMOUNT:{}".format(
            trade.externalId,
            trade.timestamp,
            trade.timestampNano,
            trade.priceStr,
            trade.amountStr,
        )
        print(trade_msg)


cw.stream.on_trades_update = handle_trades_update


# Start receiving
cw.stream.connect()

# Call disconnect to close the stream connection
# cw.stream.disconnect()