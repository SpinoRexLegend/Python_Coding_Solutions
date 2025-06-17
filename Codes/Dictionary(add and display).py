dict = {}
ch = "not yet"
print("Dont give same name twice\n")
while (ch!= "stop"):
    name = input("Enter the name: ")
    height = float(input("Please enter the height: "))
    dict[name] = height
    ch = input("Enter 'stop' to stop: ")
print(dict)
    
