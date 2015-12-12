# Singleton/ClassVariableSingleton.py
class SingleTon(object):
    __instance = None

    def __new__(cls, val):
        if SingleTon.__instance is None:
            print 'creating new object'
            SingleTon.__instance = object.__new__(cls)
        SingleTon.__instance.val = val
        return SingleTon.__instance


# creating singleton class using decorator
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
            return instances[cls]
    return getinstance


@singleton
class MySingletonClass(object):
    def __init__(self):
        print 'This is a singleton'
