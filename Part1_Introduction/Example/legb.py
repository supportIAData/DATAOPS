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

print( foo() )