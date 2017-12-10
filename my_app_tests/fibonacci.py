from my_app_tests.decorators import decorator

@decorator
def fib(n):
    result = list()
    if(type(n) is int and n>=0):
        a=0
        b=1
        for i in range(n):
            if i==0:
                result.append(a)
            if i==1:
                result.append(b)
            if i>=2:
                c=a+b
                a=b
                b=c
                result.append(c)
    else:
        result = []
    return result

#Example
#print(fib(11))
