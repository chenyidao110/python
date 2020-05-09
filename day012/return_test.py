def find_max_min(items):
    """
    :param items: list
    :return: a tuple include max and min
    """
    max_one,min_one = item[0],items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one,min_one
