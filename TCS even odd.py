from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
x=input()
x=x.split()
low=int(x[0])
high=int(x[1])
k=int(input())
l=[]
lperm=[]
count=0
d={}
lperm2=[]
for i in range(low,high+1):
    l.append(i)
res = list(product(range(low, high + 1), repeat = k))
print(res)
for i in res:
    if sum(i)%2==0:
        count+=1

##if len(l)>k:
##    #perm=combinations_with_replacement(l,k)
##    perm=permutations(l,k)
##
##    for i in perm:
##        lperm.append(i)
##    for i in range(len(lperm)):
##        if sum(lperm[i])%2==0:
##            count+=1
##else:
##    for i in range(len(l)):
##        ltest=l
##        ltest.append(l[i])
##        perm=combinations_with_replacement(ltest,k)
##        for i in perm:
##            lperm.append(i)
##    for i in lperm:
##        if i not in d.keys():
##            d[i]=1
##        else:
##            d[i]+=1
##    for i in d.keys():
##        lperm2.append(i)
##            
##
##    for i in range(len(lperm2)):
##        if sum(lperm2[i])%2==0:
##            count+=1
##        else:
##            pass
print(count)
        
    
