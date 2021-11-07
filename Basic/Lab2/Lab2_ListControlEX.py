""" List && Tuple Control Exercise """


a, b, c = 1, 2, 3

print(a, b, c)


list0 = []

list0

list01 = [1, 2, 3]
list02 = ['a', 'b', 'c']

list01
list02
len(list02)

list()
list('ABC')

list([1, 2, 3])
list((1, 2, 3))
list({1, 2, 3})

list(range(10, 20, 2))
list03 = [None]

list03 * 10
[1, 2] * 3
[1, 2]  + [3, 4]

numbers = [1, 2, 3, 4, 5]
twice = [num * 2 for num in numbers]
twice

numbers = [1, 2, 3, 4, 5]
twice = [num * 2 for num in numbers if num % 2 == 1]
twice

1,
(1, 2)
(1)
1, 2, 3
'A', 'B', 'C', 1

x = [1, 2, 3]
print(x)

a, b, c = x
d, _, f = x

print(a, b, c)
print(d, f)

## x = [1, 2, 3]
x[2] = 3.14
x

a = b = 1
print(id(a))
print(id(b))
print(id(1))

tuple_A = (1, 2, 3)
tuple_B = tuple_A

print(id(tuple_A))
print(id(tuple_B))

tuple_C = tuple_A + tuple_B
print(tuple_C)
print(id(tuple_C))

st = "Hello Wolrd!"
print(id(st))
st = st.replace("H", "h")
print(id(st))













