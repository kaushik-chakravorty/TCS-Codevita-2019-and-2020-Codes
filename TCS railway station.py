def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    return x

l=[]
ldept=[]
larrival=[]
ldept=[]
lstoppage=[]
N=int(input())
for i in range(N):
    a=input()
    a=extract(a)
    l.append(a)
for i in range(len(l)):
    ldept.append(sum(l[i]))
    larrival.append(l[i][0])
    lstoppage.append(l[i][1])
h=lstoppage.index(max(lstoppage))
count=1
for i in range(1,N):
    if larrival[i] in range(larrival[h],ldept[h]+1) and ldept[i] in range(larrival[h],ldept[h]+1):
        pass
    else:
        count+=1
print(count)

    
