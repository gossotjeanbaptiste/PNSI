a=1

def f1():
    vf1=99
    print(a)
    print(vf1)


def f2():
    a=33
    print(a)
    print(vf1)

def f3():
    a=87
    print(a)

def f4():
    a=a+1

def f5():
    global a
    a=33
    print(a)

print(a)
