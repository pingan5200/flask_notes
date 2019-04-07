import functools


try:
    from greenlet import getcurrent as get_ident
except:
    from threading import get_ident


# 为每个线程开辟空间
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


# 把local列表维护成一个栈
class LocalStack(object):
    def __init__(self):
        self._local = Local()

    def push(self, value):
        rv = getattr(self._local, 'stack', None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(value)
        return rv

    def pop(self):
        stack = getattr(self._local, 'stack', None)
        if stack is None:
            return None
        elif len(stack) == 1:
            return stack[-1]
        else:
            return stack.pop()

    def top(self):
        try:
            return self._local.stack[-1]
        except (AttributeError, IndexError):
            return None

# xxx = LocalStack()
# xxx.push('佳俊')
# xxx.push('咸鱼')
# print(xxx.pop())


# 封装request和session
class RequestContext(object):
    def __init__(self):
        self.request = "xx"
        self.session = "oo"


# 获取request和session  
def get_request_or_session(arg):
    ctx = xxx.top()
    return getattr(ctx, arg)


# obj = xxx.top()
# print(obj.request)
# print(obj.session)

xxx = LocalStack()
xxx.push(RequestContext())
# 偏函数，自动传递参数
request = functools.partial(get_request_or_session, 'request')
session = functools.partial(get_request_or_session, 'session')

print(request())
print(session())
