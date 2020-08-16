#l=['*.*#***#***#***.*.','*.*#*.*#.*.#******','***#***#***#****.*']
l=[]
lindex=[]
n=int(input())
for i in range(3):
    a=input()
    l.append(a)
for i in range(len(l)):
    for j in range(len(i)):
        if l[i][j]=='#':
            lindex.append(j)
index=len(lindex)
for i in range(len(l)):
    for j in range(lindex[i]):
        
        
    
