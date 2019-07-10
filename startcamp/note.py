a=[1,2,3,4]
print(a.append(5))
print(a)
a.pop(3)
print(a)

print(4 in a)

for id, item in enumerate(a):
    print(f'hello{id} i am {item}')


b=[item*3 for item in a]
print(b)
print(b[2:-4])