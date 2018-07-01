import hashlib
import functools

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
