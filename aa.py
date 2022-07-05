from itertools import chain

a = [(1, 'a'), (2, 'b'), (3, 'c')]
b = [[1, 2], [3, 4], [5, 6]]
c = [{1, 2}, {3, 4}, {5, 6}]

for x in [a, b, c]:
    print(list(chain(*x)))
