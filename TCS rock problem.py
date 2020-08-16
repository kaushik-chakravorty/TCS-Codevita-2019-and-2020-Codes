##helping a spanish guy to sort rocks!
##.split() basically helps to get rid of all spaces
lrange=[]
def solved(x):
    l=x.split()
    for i in range(len(l)):
        l[i]=int(l[i])
    return l
        
s=input()
ls=solved(s)
sizelist=input()
lsize=solved(sizelist)
for i in range(ls[1]):
    x=input()
    lx=solved(x)
    lrange.append(lx)
a=str()
for i in range(len(lrange)):
    count=0
    
    
    for j in range(len(lsize)):
        if lsize[j] in range(lrange[i][0],lrange[i][1]):
            count+=1
    a=a+' '+str(count)
print(a)


