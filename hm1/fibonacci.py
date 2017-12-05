def fib(n):
    a=0
    b=1
    for i in range(n):
        if i==0:
            print(a),
        if i==1:
            print(b),
        if i>=2:
            c=a+b
            a=b
            b=c
            print(c),
#Example
# fib(11)
