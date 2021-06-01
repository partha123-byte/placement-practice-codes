


def find(order,nuts,list):

    for i in order:
         if i in nuts:
            list.append(i)



n=int(input())
a=input()                                            ### ! # $ % & * @ ^ ~
b=input()

nuts=a.split(",")
bolds=b.split(",") 
list=[]
list3=[]
order=["!","#","$","%","&","*","@","^","~"]

find(order,nuts,list)
find(order,bolds,list3)

print(list)
print(list3)


#time complexity n