import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)

    client = get_client()

    print("Placing Order...")
    print(vars(args))

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Successful")

    print("Full Response:", order)
    print("OrderId:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("ExecutedQty:", order.get("executedQty"))
    print("AvgPrice:", order.get("avgPrice"))

except Exception as e:

    print("Order Failed:", e)