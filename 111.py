def simple_sort(data):
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:
    """

    def ex(a, b):
        swap = a
        b = a
        a = swap
        return a, b

    for i in range(len(data)):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = ex(data[i], data[i + 1])
    return data


d = [1, 3, 5, 8, 9, 2, 7, 4, 6]
print(simple_sort(d))

