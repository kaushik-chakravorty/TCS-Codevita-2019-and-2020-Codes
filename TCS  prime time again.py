def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    D=x[0]
    P=x[1]
    if D%P==0:
        return D,P
    else:
        print('invalid input')
def is_prime(x):
    count=0
    if x!=0 and x!=1:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                count+=1
            else:
                pass
        if count==0:
            return 1

n=input()
count=0

D,P=extract(n)
parthours=D//P
for i in range(parthours):
    l=[]
    for j in range(P):
        result=is_prime(i+parthours*j)
        if result==1:
    
            l.append(1)
        else:
            pass
    if len(l)==P:
        count+=1
        
        
    else:
        pass
    
print(count)
