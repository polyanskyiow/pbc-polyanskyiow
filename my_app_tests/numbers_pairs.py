def decorator(func):
    def wrapper(*args):
        for a in args:
            print 'arg: "{}"'.format( a)
        rs = func(*args)
        return rs
    return wrapper

@decorator
def print_pairs(*args):
    l=0
    m=l+1
    result = set()

    for l in range(args.__len__()-1):
        for m in range(args.__len__()):
            if( l!= m and args[l] + args[m] == 10):
                if (args[l] > args[m]):
                    result.add((args[m], args[l]))
                else:
                    result.add((args[l], args[m]))
    return result

#Example
#print(print_pairs(2,7,5,3,1,5,9,8,1))