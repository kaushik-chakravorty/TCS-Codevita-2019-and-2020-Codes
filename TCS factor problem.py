##kth largest factor of m
def extract(x):
    l=x.split(',')
    for i in range(len(l)):
        l[i]=int(l[i])
    #print(l)
    return l
a=input()
l1=extract(a)
##l1=[30,9]
n=l1[0]
k=l1[1]

lfactor=[]
for i in range(1,n+1):
    if n%i==0:
        lfactor.append(i)
if k>len(lfactor):
    print('1')
else:
    
    print(lfactor[k])
