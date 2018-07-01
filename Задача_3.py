import functools

def decor(func):
    @functools.wraps(func)
    def inner(arg, x='Farewell!'):
        new_arg=x        
        x=arg*3
        return func(new_arg, x)
    return inner

def F_F(arg, x='Hello!'):
    print(x)
    return(arg)

print(F_F(33))
print('----------')
print(decor(F_F)(33))
