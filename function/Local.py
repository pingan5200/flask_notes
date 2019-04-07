# 为每个线程开辟内存空间

try:
    from greenlet import getcurrent as get_ident
except:
    from threading import get_ident


class Local(object):
    def __init__(self):
        # storage = {1231:{'stack':[]}}
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, key, value):
        # 获取线程唯一标识
        ident = get_ident()
        if ident not in self.storage:
            self.storage[ident] = {key: value}
        else:
            self.storage[ident][key] = value

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.storage:
            return self.storage[ident].get(item)

obj = Local()
obj.stack = []
obj.stack.append('佳俊')
obj.stack.append('咸鱼')
print(obj.stack)
print(obj.stack.pop())
print(obj.stack)
