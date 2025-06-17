from math import factorial
def PascalTriangle(row):
    if row <= 0:
        return "\nInvalid Input"  
    for i in range(row):
        for j in range(i):
            S =(int) (factorial(i)/(factorial(j) * factorial(i-j)))
            print(S, end = "    ")
        print("1")
        print("\n")
    return "Suceesfully printed"
print(PascalTriangle(int(input("Enter the no of rows: "))))
