n=int(input())
a=input()                                            ### ! # $ % & * @ ^ ~
b=input()

nuts=a.split(",")
bolds=b.split(",") 
list=[]
list3=[]
                                                     #nuts=[%,#,*,!] 
order=["!","#","$","%","&","*","@","^","~"]
                                                     
for i in order:
    
    for j in nuts:
        if(i==j):
            list.append(j)
            break


                                                            
    
for i in order:
    
    for j in bolds:
        if(i==j):
            list3.append(j)
            break

                                            
                                                                            
                                                                        
             



print(list)
print(list3)

#solved