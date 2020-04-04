x = "global"


def foo():
    print(x)


def bar():
    global x
    x = x * 2
    print(x)


foo()
print(x)
bar()
