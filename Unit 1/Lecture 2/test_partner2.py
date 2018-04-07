def powerset(items):
    from itertools import chain, combinations
    for j in chain.from_iterable(combinations(items, n) for n in range(len(items)+1)):
        yield j

def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    f = powerset(a)

    posible = []

    for i in range(2**len(a)):
        e = f.__next__()
        assert e not in posible, "not correct"
        posible.append(e)
        print(i, e)

main()
