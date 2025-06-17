import math
def main():
    m,n = int(input()), int(input())
    if(m>1 and m<501 and  n>1 and  n<501):
        x = (m*n)/2
        print(math.ceil(x))
    else:
        print("Null")

main();