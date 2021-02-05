#With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

a=int(input("enter a number"))
num=1
lst=[]
while len(lst)<a:
    if(num%2 !=0):
        lst.append(num)
    num+=1

print(lst)
         
