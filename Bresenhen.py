def Bres(x,y,x2,y2):
    x1=x
    y1=y
    dx=x2-x1
    dy=y2-y1
    p=(2*dy)-dx
    while(x<=x2):
        print(x,y)
        x=x+1;
        if(p<0):
            p=p+(2*dy)
        else:
            p=p+(2*dy)-(2*dx)
            y=y+1
Bres(5,5,12,10)    