import functools

z=0
def once(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		if not inner.called:
			inner.result = func(*args, **kwargs)
			inner.called = True

		return inner.result

	inner.called = False
	return inner

@once
def initialize_settings():
  global z
  print(z)
  print("Settings initialized")
  z+=1
  return z


print(initialize_settings())
print('-----------')
print(initialize_settings())
print(z)

#не вижу что тут тестировать...