from interfaceAuto.atf.util.logUtil import  Logger

def Deprecated(func):
    def wrapper(*args, **kwargs):
        Logger().warning("this method " + func.__name__ + " is Deprecated! Please choose another to use!")
        return func(*args, **kwargs)

    return wrapper