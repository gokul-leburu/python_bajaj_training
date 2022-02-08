def MaxthreeNum(a,b,c):
    return max(a,b,c)
def sumallelm(l):
    return sum(l)
def prod(l):
    product=1
    for i in l:
        product*=i
    return product
def reversestr(s):
    return s[::-1]
def factorial(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product
def rangefall(n,a,b):
    if(n>=a and n<=b):
        return "yes falls in the range"
    else:
        return "do not fall in the range"
def evennolist(l):
    temp=[]
    for i in l:
        if(i%2==0):
            temp.append(i)
    return temp
print(MaxthreeNum(2, 3, 1))
print(sumallelm([8,2,3,0,7]))
print(prod([8,2,3,-1,7]))
print(reversestr("1234abcd"))
print(factorial(5))
print(rangefall(24, 20, 25))
print(evennolist([1,2,3,4,5,6,7,8,9,10]))
