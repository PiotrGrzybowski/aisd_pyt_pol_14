class A:

    def __len__(self):
        pass

    def __add__(self, other):
        pass

    def __str__(self):
        pass

    def __bool__(self):
        pass

    def __contains__(self):
        pass


values: list = [5, 4, 8]
print(len(values))
print(str(values))
print(repr(values))

print([4, 5] + [1, 2])

if 5 in values:
    print('contains')

if values.__contains__(5):
    print('contains')

for value in values.__iter__():
    print(value)
