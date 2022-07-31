import math
def test(a):
    dist=[]
    n=len(a)
    i=0
    j=0
    while(i<n):
        d=0
        j=0
        while(j<n):
            x=abs(a[i][0]-a[j][0])+abs(a[i][1]-a[j][1])
            d=d+x
            j=j+1
        dist.append(d)  
        i=i+1
    print(dist)
    return(min(dist))   

x=test([[9,9],[7,8]])
print(x)