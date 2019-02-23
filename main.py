## Example list


my_list = ["ena", "dio", "tria", "tesera",10]
iterator = 0
for item in my_list:
    iterator+=1
    if type(item)==str:
        print("the  string length is : "+str(len(item)))
    else:
        print("the %d intex type is : %s" %(iterator, str(type(item))))

input()