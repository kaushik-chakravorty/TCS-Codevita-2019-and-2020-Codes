def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    return x
T=int(input())
for i in range(T):
    l=[]
    lgift=[1]

    n=int(input())
    l=input()
    l=extract(l)
    l.sort()
    for i in range(1,len(l)):
        if l[i]>1 and l[i]==l[i-1]:
            lgift.append(l[i-1]-1)

        elif l[i-1]==l[i]:
            lgift.append(l[i-1])

        
        elif l[i]>l[i-1]:
            lgift.append(lgift[i-1]+1)
        else:
            pass
    print(lgift)
    print(sum(lgift))
