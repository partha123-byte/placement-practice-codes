inp=input()
list2=[]
for i in inp:
    if(i==" "):
        list2.append(i)

    elif(i=="w"):
        list2.append("a")
    elif(i=="x"):
        list2.append("b")
    elif(i=="y"):
        list2.append("c") 
    elif(i=="z"):
        list2.append("d")       

    else:    
        list2.append(chr(ord(i)+4))

print(list2)

print("".join(list2))    