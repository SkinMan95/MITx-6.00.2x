def powerSet2(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 0:
        yield []
    else:
        for item in powerSet2(seq[1:]):
            yield [seq[0]]+item
            yield item    


items = 'abcdefghij'
count = 0
pos = []
for i in powerSet2(items):
    count += 1
    assert i not in pos, "not correct"
    pos.append(i)
    print(i)
print("len of items is {}".format(count))
