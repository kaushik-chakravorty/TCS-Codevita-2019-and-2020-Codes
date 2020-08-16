from itertools import permutations
T=int(input())

def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    return x
def checker(l,n):
    lperm=[]
    count=0
    a=permutations(l)
    for i in a:
        lperm.append(list(i))

    if len(lperm)<10**4:
        
        for i in range(len(lperm)):
            count=0
            for j in range(n):
                
                if j+1<=n-1:
                    if (lperm[i][j]+lperm[i][j+1])%3==0:
                        count+=1
            if count==0:
                return 'Yes'
            else:
                pass
        if count!=0:
                return 'No'
    else:
        
            
    
for i in range(T):
    N=int(input())
    arr=input()
    if N<=10**3:
        arr=extract(arr)
        c=checker(arr,N)
print(c)
