# Graphics_algos 
# Copyrighted under MIT 
# author : V.EswarChand
# don't change anything here.


def Bres(x,y,x2,y2):
    x1=x
    y1=y
    dx=x2-x1
    dy=y2-y1
    p=(2*dy)-dx
    while(x<=x2):
        print("X: ",x,"  Y: ",y)
        x=x+1;
        if(p<0):
            p=p+(2*dy)
        else:
            p=p+(2*dy)-(2*dx)
            y=y+1
def Bresenhen_Algo():
    X=int(input("Enter the value of X: "))
    Y=int(input("Enter the value of Y: "))
    X1=int(input("Enter the value of X1: "))
    Y1=int(input("Enter the value of Y1: "))
    print("The values of the Bresenhen Line Drawing Algorithms are.....")
    Bres(X,Y,X1,Y1)   
    
Bresenhen_Algo()
