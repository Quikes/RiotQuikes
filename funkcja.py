def cache(fn):
    c = {}

    def inner(*args):
        if c.get(f'{args}',None) is None:
            print('cache')
            c[f'{args}'] = fn(*args)
        return c[f'{args}']

    return inner



@cache
def add(a,b):

    x = [x * x for x in range(10000000)]


    return a+b

@cache
def add_three(a,b,c):

    x = [x * x for x in range(10000000)]


    return a+b+c


add(1,2)
add(1,2)
add(1,2)
add(1,2)

add_three(1,2,3)
add_three(1,2,3)
add_three(1,2,3)
add_three(1,2,3)


# def add (a,b):
#     x = [x * x for x in range(10000000)]
#     return a + b 

# print(add(1,2))
# print(add(1,3))

# print(add(2,2))
# print(add(1,2))
# print(add(1,3))

# print(cache)

# def sentence(name):
#     def inner(city):
#         return f'{name} - {city}'
#     return inner

# full_sentence = sentence('pawel')
# print(full_sentence('krakow'))


def gen_uuid():
    idx=0

    def inner(new_id=None):
        nonlocal idx
        if new_id is not None:
            idx = new_id
        result = idx
        idx +=1
        return result
    return inner


def g():
    idx = 0
    while True:
        yield idx
        idx+=1




