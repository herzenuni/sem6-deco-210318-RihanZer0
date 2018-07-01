import functools
import pytest

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

@pytest.mark.parametrize("x,expected", [
    (11,11),
    (22,22),
    (66,66),
    (99,99)])
def test_F_F(x, expected):
    assert F_F(x) == expected

@pytest.mark.parametrize("a,b,expected", [
    (1,11,11),
    (2,22,22),
    (6,66,66),
    (9,99,99)])
def test_decor(a,b, expected):
    assert decor(F_F)(a,b) == expected