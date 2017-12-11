def log(func):
    def wrapper(*args):
        print(func.__name__ ),
        if(args.__len__() == 1):
            print("(" + str(args[0]) + ")")
        else:
            print(args)
        rs = func(*args)
        return rs
    return wrapper