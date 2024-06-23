import re

regex = re.compile("[^a-zA-Z]")

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) is not str:
        return -1

    if skus == '':
        return 0

    cleaned_skus = regex.sub('', skus).upper()
    if cleaned_skus == '':
        # illegal input
        return -1

    item_names = prices.keys()


    # count items
    # apply discounts & calculate total
    pass


