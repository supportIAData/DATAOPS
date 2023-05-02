# G espace global
a = 101
b = 22


def foo():
    b = 1
    # E englobant puis il remonte

    def baz():
        # Python b regarde localement L
        print(b)
        print(a)

    baz()


print(foo())


def g(*t):
    return t


print(g(1, 2, 3, 7, 8, 10))  # 1,2,3


def h(**t):
    return t


print(h(a=2, b=8, c=10))


print(range(1, 1000))


# for i in range(1,1000):
#     print(i)

print(zip([1, 2, 3], [8, 9, 10]))

for e in zip([1, 2, 3], [8, 9, 10]):
    print(e)

l = list(range(1, 10))

print(l)

# start:end:step

print(l[::2])

# step de 2
print(l[:2])

# 7 8 9
print(l[-3:])

# 2 3 4
print(l[1:4])

print(l[::-1])


# shallow copy copie peu profonde

r = [1, 2, 67]

s = r

s[0] = 100 

print(r)
print(s)

# ------
r = [1, 2, 67]

s = r[:]

s[0] = 100 

print(r)
print(s)

print("--------")

q = [[1, 2], [3, 9]]

t = q[:]

t[0][0] = 100
print(q)
print(t)