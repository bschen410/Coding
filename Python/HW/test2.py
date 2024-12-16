def outer():
    yield from a(0)
    # yield 0
    # yield 1
    yield "abc"


def a(b):
    yield 0
    yield 1


for i in outer():
    print(i)
