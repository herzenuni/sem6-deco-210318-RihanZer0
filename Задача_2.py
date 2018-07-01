import functools

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
  print("Settings initialized")
  z=0
  z+=1
  return z


print(initialize_settings())
print('-----------')
print(initialize_settings())
