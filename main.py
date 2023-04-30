a, *b  = 'dsdsd','asas'

# / всё что слева - только позиционные аргументы           (1)
# * всё что справа - только ключевые (keyword) аргументы   (a=1) args
# *args соберает все позициионные аргументы в кортеж
# **kwargs соберает все keyword аргументы в словарь

def example(a, /, b, *, c):
    print(f'{a}')
    print(f'{b}')
    print(f'{c}')

def my_print(*args, **kwargs):
    
    print(f"Got keywords: {kwargs}")

    print(args)
    for item in args:
        print(str(item), **kwargs)
   


if __name__ == "__main__":
    
    # example(1,2, c=3)
    my_print(1,2,3,4,5,6,7, sep=":", end="-")
    # print(1,2, **{'sep':":", 'end':"-"})
    # print(1,2, sep=':', end='-')

    # print(a)
    # print(b)

    print(f'{a=}')
    print(f'{b=}')
    # print(f'{c=}')
    # print(*[1,2,3,4])

