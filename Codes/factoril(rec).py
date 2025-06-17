def fac(a):
    
    if a==0:
        return 1
    return a * fac(a-1)

def prim(a):
    k = 0
    for i in range (2, a//2 + 1):
        if(n%i == 0):
            k += 1
    if k <= 0:
        print("prime")
    else:
        print("Not prime")
        
#__main__
n = int(input("The number is: "))
ch = int(input("1 for factorial\n2 for prime number\nEnter your choice: "))
if ch == 1:
    print(fac(n))
elif ch == 2:
    print(prim(n))
