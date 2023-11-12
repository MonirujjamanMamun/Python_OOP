def first():
    print("hello")


first()


def sum(n1, n2):
    mul = n1*n2
    print(mul)


sum(11, 2)


def ferot(num1, num2):
    res = num1+num2
    return res


total = ferot(55, 55)
print(total)


def defal_arg(num1, num2, *args):
    print(args)
    restul = num1+num2
    return restul


ans = defal_arg(50, 20)
print(ans)
