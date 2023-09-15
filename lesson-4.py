def black_hole(*args):
    print(type(args))
    for i in args:
        print(i)


def black_hole_named(**kwargs):
    print(type(kwargs))
    for i in kwargs:
        print(i)


def black_hole_mixed(var_1, var_2=3, *args, **kwargs):
    print("var_1 = ", var_1)
    print("var_2 = ", var_2)
    for arg in args:
        print("arg = ", arg)
    for key, value in kwargs.items():
        print("key = ", key, ", value = ", value)

def way(s, t):
    return s * t;

def some_fun(var_1, var_2, var_3, var_4):
    print(var_1, var_2, var_3, var_4)

dict_1 = {"var_3":3, "var_4":4}
list_1 = [2]
some_fun(1, *list_1, **dict_1)

# list_1 = [60, 9]
# dict_1 = {"s":60, "t":9}
# print(way(*list_1))
# print(way(**dict_1))

# black_hole(1 ,34, 3, "Cat", 3)
# black_hole_named(name="Denis", age=21)
# black_hole_mixed(3, 4, "Cat", 34, name="Denis", age=21)