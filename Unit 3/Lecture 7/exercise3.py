def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    mean = 0.0
    for e in L:
        assert isinstance(e, str), "not all elements in list is of type str"
        mean += len(e)
    mean /= len(L)

    s = 0
    for e in L:
        s += (len(e) - mean)**2

    return (s / len(L))**0.5

def main():
    EPS = 1e-4
    d = stdDevOfLengths(['a', 'z', 'p'])
    assert abs(d) < EPS, "{}".format(d)

    d = stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
    assert abs(d - 1.8708) < EPS, "{}".format(d)
    
main()
