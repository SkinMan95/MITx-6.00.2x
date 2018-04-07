import itertools

def powerSet(items):
    N = len(items)
    for i in range(N+1):
        iterator = itertools.combinations(items, i)
        for combo in iterator:
            yield list(combo)
        
def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    f = powerSet(a)

    posible = []

    for i in range(2**len(a)):
        e = f.__next__()
        assert e not in posible, "not correct"
        posible.append(e)
        print(i, e)

main()
