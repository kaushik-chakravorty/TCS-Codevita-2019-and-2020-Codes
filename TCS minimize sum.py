def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    return x
##def sorting(l):
##    for i in range(l):
        
nk=input()
nk=extract(nk)
n,k=nk[0],nk[1]
lint=input()
lint=extract(lint)


for i in range(k):
    lint.sort()
    lint.reverse()
    lint[0]=int(lint[0]/2)

print(sum(lint))
    
