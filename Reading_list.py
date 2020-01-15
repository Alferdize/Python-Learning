import math
def foo():
    pass
a = [1, 2, 3, 5]
b = [5, 3, 2, 1]
print(a == b)
print(a is b)
c = [int, len, foo, math]
foo
print(a[::-1])
# a += ['grault', 'garply']
print(a)
a *= 2
print(max(a))
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x[0], x[2], x[4])

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
a[1:5] = []
print(a)
a += 'happy'
print(a)

# Append and extend are not same

# extend
a = ['a', 'b']
a.extend([1, 2, 3])
a

print(a)

# append

a = ['a', 'b']
a.append(['foo'])
print(a)



# insert
 

a.insert(2,56)
print(a)







