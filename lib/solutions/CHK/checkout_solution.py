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
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "E": [(2, "B")]
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

        while item_count > 0:
            if item_discount := discounts.get(item_name):
                for discount in item_discount:
                    discount_count, discount_price = discount

                    remainder = item_count % discount_count
                    if remainder == item_count:
                        continue

                    if remainder == 0:
                        total += (item_count // discount_count) * discount_price
                        break

                    total += remainder * item_price
                    if type(discount_price) is int:
                        total += (item_count // discount_count) * discount_price

                    elif type(discount_price) is str:
                        total += (item_count // discount_count) * prices[discount_price]

                    item_count -= remainder
                    continue

            # no discounts to apply
            else:
                total += item_count * item_price
                break

    return total


