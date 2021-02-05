a=int(input("Enter a number"))
if a%2==0:
    a=a-1
num=1
lst=[]
while len(lst)<a:
    if(num%2 !=0):
        lst.append(num)
    num+=1
print(lst)
