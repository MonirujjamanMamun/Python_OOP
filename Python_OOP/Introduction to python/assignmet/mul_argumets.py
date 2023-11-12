
def pass_mult_agrs(*args):
    # we can do our work in here
    for arg in args:
        print(arg)


pass_mult_agrs(10, 20, 30, 40)


def pass_kagrs(**kagrs):
    for key, value in kagrs.items():
        print(key, ':', value)


pass_kagrs(name='potol', title='khan', age=20)
