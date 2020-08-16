
def get_prime(n):
    l=[]
    for i in range(2,n):
        count=0
        for j in range(2,i+1):
            if i!=j:
                if i%j==0:
                    count+=1
                else:
                    pass
        if count==0:
            l.append(i)
    return l
        
def consecutive_prime(l,n):
    primes=set(l)
    l1=[]
    
    for i in range(0,len(l)):
        a=l[i]
        for j in range(i+1,len(l)):
            a=a+l[j]
            if a<=n:
                
            
                if a in primes:
                    l1.append(a)
            else:
                break
    return l1    
n=int(input('enter the upper limit'))
l=get_prime(n)
l1=consecutive_prime(l,n)
print(len(l1))
