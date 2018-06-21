import hashlib
import functools

@functools.singledispatch
def hash(arg):
    type_name = type(arg).__name__
    assert False, "Неподдерживаемый тип объекта: " + type_name

@hash.register(str)
def _(arg):
    result = hashlib.md5(bytes(arg,'utf-8')).hexdigest()
    return result

@hash.register(list)
def _(arg):
    result = type(arg)()
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return result

@hash.register(tuple)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return tuple(result)

@hash.register(set)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return set(result)

@hash.register(dict)
def _(arg):
    keys = arg.keys()
    values = []
    for i in arg.values():
        values.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    result = dict.fromkeys(keys,None)
    result.update(zip(keys,values))
    return result

print(hash('Nanomachines, son!'))
print(hash(["It's", 'ALIVE']))
print(hash(("It's", 'INSANE')))
print(hash({"It's", 'MAD'}))
print(hash({'ALIVE':'ALIVE', 'INSANE':'INSANE', 'MAD':'MAD'}))