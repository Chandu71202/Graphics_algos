l=[]
z=[]
for i in range(8):
    x=int(input())
    l.append(x)

n=input("Enter which Shearing: ")
def Shearing(n):
   
    a=int(input("Enter shearing value :"))
    if(n=="x"):
        for i in range(8):
            if(i%2==0):    
                b=l[i]
                b=b+a*l[i+1]
                z.append(b) 
    else:
        for i in range(8):
            if(i%2!=0):    
                b=l[i]
                b=b+a*l[i-1]
                z.append(b) 
Shearing(n)
for i in range(4):
    if(n=="x"):
        print(z[i],l[i*2+1])
    else:
        print(l[i*2],z[i])