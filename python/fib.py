#print the fibonacci numbers up the input number
def fib(n,x):
    for i in range(2,n):
        sum=x[i-1]+x[i-2]
        x.append(sum)
    return x
x=[0,1]
n=int(input("enter the number"))
k=fib(n,x)
print(k)