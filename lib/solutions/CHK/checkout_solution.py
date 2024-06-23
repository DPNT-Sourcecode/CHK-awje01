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

    cleaned_skus = regex.sub('', skus)
    if cleaned_skus == '':
        return

    

    # clean input
    # check for valid input
    # count items
    # apply discounts & calculate total
    pass

