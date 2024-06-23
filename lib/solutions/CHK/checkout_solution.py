import re

regex = re.compile("[^a-zA-Z]")

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
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
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    if type(skus) is not str:
        return -1

    if skus == '':
        return 0

    cleaned_skus = regex.sub('', skus).upper()
    if cleaned_skus == '':
        # illegal input
        return -1

    total = 0
    item_names = prices.keys()
    for item_name in item_names:
        item_price = prices[item_name]
        item_count = skus.count(item_name)

        # apply discount
        if item_discount := discounts.get(item_name):
            remainder = item_count % item_discount["count"]
            total += (remainder * item_price) + item_discount["price"] * (item_count - remainder)

        else:
            total += item_count * item_price

    return total


