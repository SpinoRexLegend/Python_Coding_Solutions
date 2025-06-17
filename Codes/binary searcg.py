def binary_search(Lst):
    #considering it to be a sorted list
    length = len(Lst)
    mid = length//2
    find = int(input("Enter the element u wanna find: "))
    while(mid > 0 and mid < length):
        if Lst[mid] > find :
            mid /=2#forgot to iclude upper and lower limits
        elif Lst[mid] < find :
            mid = mid + (mid//2)
        else:
            return Lst[mid]
        
def initialisation():
    L =[]
    l = int(input("Please enter the no of elements u wannna add: "))
    for i in range(l):
        nig = int(input("Enter the element:"))
        L.append(nig)
    print(binary_search(L))

initialisation()
