def main(*args, **kwargs):
    print("Hello World")
    print("args", args)
    print('kwargs', kwargs)


# main(1, 2, 3, x=4, y=5, z=6)


def ppprint(*args):
    print(*args)
    return len(args)

a = ppprint('Hello ', 'world', '!', 2, 4)
print(a)