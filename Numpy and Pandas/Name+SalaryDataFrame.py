import pandas as pd
dick = {}
c = 1
name = []
salary = []
while (c != 0):
    name.append(input("Enter the bandes name: "))
    salary.append(float(input("Enter the bandes salary: ")))
    c = int(input("Press 0 to stop: "))
    print()
dick = {'Name': name, 'Salary': salary}
dick = pd.DataFrame(dick)
print(dick)


