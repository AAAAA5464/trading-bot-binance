from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():

    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    client = Client(api_key, secret_key)

    # Binance Futures Testnet endpoint
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client