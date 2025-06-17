input_string = input("Intervals =  ")
my_list = eval(input_string)
my_list.sort()
flag="True"
i=0
while flag=="True":
    if i<len(my_list)-1:
        if my_list[i][1]>my_list[i+1][0]:
            flag="False"
            break;
    else:
        break;
    i+=1
print(flag)
