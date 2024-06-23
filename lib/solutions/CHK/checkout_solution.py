import re

regex = re.compile("[A-Z]+$")

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

discounts = {
    "A": {
        "count": 3,
        "price": 130
    },
    "B": {
        "count": 2,
        "price": 45
    },
    "E": {
        "count": 2,
        "price": "B"
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    if type(skus) is not str:
        return -1

    if skus == '':
        return 0

    if not regex.match(skus):
        return -1

    total = 0
    item_names = prices.keys()
    for item_name in item_names:
        item_price = prices[item_name]
        item_count = skus.upper().count(item_name)

        # apply discount
        if item_discount := discounts.get(item_name):
            remainder = item_count % item_discount["count"]

            discount_price = item_discount["price"]
            if type(discount_price) is int:
                total += (item_count // item_discount["count"]) * discount_price

            elif type(discount_price) is str:
                total += (item_count // item_discount["count"]) * prices[discount_price]

            if remainder != 0:
                total += remainder * item_price

        # no discounts to apply
        else:
            total += item_count * item_price

    return total


