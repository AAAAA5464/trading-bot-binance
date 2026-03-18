# Binance Futures Trading Bot (Testnet)

This is a CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI input using argparse
- Logging of API requests and responses
- Error handling

## Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── bot.log


## Setup

Install dependencies:
pip install -r requirements.txt

Create `.env` file:

BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key

# To Run
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 74000

## Assumptions

- Binance Futures Testnet is used.
- API keys are loaded from .env.
- LIMIT orders require a price argument.
