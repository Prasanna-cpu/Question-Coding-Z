def is_fib(num):
    fibs=[0,1]

    a,b=0,1
    while b<=num:
        a,b=b,a+b
        fibs.append(b)

    return num in fibs


def filter_fibonacci(numbers):
    result=[]
    for num in numbers:
        if is_fib(num):
            result.append(num)

    return result