
class Foo(object):
    def __init__(self):
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, key, value):
        print(key, value, self.storage)


obj = Foo()
obj.xx = 123
