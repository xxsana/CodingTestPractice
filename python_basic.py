# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''Type Hint'''
a: str = "1"
print(type(a))

'''list comprehension'''
print('-----------------------list comprehension-----------------------')
b = [ 2*x for x in range(1, 10+1)]
print(b)

# with if keyword
c = [ x for x in range(1, 10+1) if x % 2 == 0]
print(c)

d = [ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
print(d)

e = [ x for x in range(10) if x < 5 if x % 2 == 0]
print(e)


'''Generator'''
print('-----------------------generator-----------------------')
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

print(get_natural_number())

f = get_natural_number()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

def generator():
    yield 1
    yield 'string'
    yield True

g = generator()
print(next(g))
print(next(g))
print(next(g))

