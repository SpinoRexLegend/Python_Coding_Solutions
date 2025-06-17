l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
if (l >= 0 and b >= 0):
    print("-"*b)
    for i in range (l):
        st = "|" + (" "*(b-2)) + "|"
        print(st)
    print("-"*b)
else:
    print("invalid numbers")
