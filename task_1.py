import hashlib
import functools
import pytest

@functools.singledispatch
def magic(arg):
    type_name = type(arg).__name__
    assert False, "Неподдерживаемый тип объекта: " + type_name

@magic.register(str)
def _(arg):
    result = hashlib.md5(bytes(arg,'utf-8')).hexdigest()
    return result

@magic.register(list)
def _(arg):
    result = type(arg)()
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return result

@magic.register(tuple)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return tuple(result)

@magic.register(set)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return set(result)

@magic.register(dict)
def _(arg):
    keys = arg.keys()
    values = []
    for i in arg.values():
        values.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    result = dict.fromkeys(keys,None)
    result.update(zip(keys,values))
    return result

print(magic('Nanomachines, son!'))
print(magic(["It's", 'ALIVE']))
print(magic(("It's", 'INSANE')))
print(magic({"It's", 'MAD'}))
print(magic({'ALIVE':'ALIVE', 'INSANE':'INSANE', 'MAD':'MAD'}))

@pytest.mark.parametrize("x,expected", [
    ('Nanomachines, son!','49d5591cd06e13329d1eaea734049a0e'),
    (["It's", 'ALIVE'],['398860b910c8290e32073604b943042c', '3bfa0eed9e858c516e816a519b2a82eb']),
    (("It's", 'INSANE'),('398860b910c8290e32073604b943042c', '388cab806b9cf0a7406a6f2b39360da8')),
    ({"It's", 'MAD'},{'398860b910c8290e32073604b943042c', '93720e823d9d9af2323095152cb82906'}),
    ({'ALIVE':'ALIVE', 'INSANE':'INSANE', 'MAD':'MAD'},{'ALIVE': '3bfa0eed9e858c516e816a519b2a82eb', 'INSANE': '388cab806b9cf0a7406a6f2b39360da8', 'MAD': '93720e823d9d9af2323095152cb82906'})
])
def test_param(x, expected):
    assert magic(x) == expected