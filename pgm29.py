mylist=[]
n=int(input())
#a,b,c=int(input().split())
for i in range(n):
    #x=input()
    x= [input(), int(input())] 
    mylist.append(x)
   
for i in range(len(mylist)):    
    print(mylist[i],i)
          
