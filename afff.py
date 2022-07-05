def test(a: int, *b, c: int):
    print(a, b, c)
    print('b type is ', type(b))


test(1, 2, 3, 4, c=10)

a, *b, c = (1, 2, 3, 4, 10)
print(a, b, c, end='\n\n')