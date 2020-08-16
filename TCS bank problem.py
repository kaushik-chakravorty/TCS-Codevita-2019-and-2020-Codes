##bank problem
def solved(x):
    l=x.split()
    for i in range(len(l)):
        if len(l[i])>2:
            l[i]=float(l[i])
        else:
            l[i]=int(l[i])
            
        
    return l
        
def EMIX(lx,pX,t):
    x=pX
    for i in range(len(lx)):
        for j in range(lx[i][0]):
            pX=pX+(pX*lx[i][1])/100
    surplusX=pX-x
    miX=surplusX*100/(x*t*12)
    y=1/((1+miX)**(t*12))
    emiX=x*miX/(1-y)
    return emiX


l1=[]
l2=[]

##for 1st test case
##p=10000
##t=20
##n1=3
##n2=3


p=int(input('enter loan amount'))
t=int(input('enter tenure'))
n1=int(input('enter slabs for a'))
for i in range(n1):
    a=input('enter interest rate nad their period')
    a=solved(a)
    l1.append(a)
print(l1)
n2=int(input('enter slabs for b'))
for i in range(n2):
    b=input('enter interest rate nad their period')
    b=solved(b)
    l2.append(b)

##l1=[[5,9.5],[10,9.6],[5,8.5]]
##l2=[[10,6.9],[5,8.5],[5,7.9]]

##for 2nd test case
##p=500000
##t=26
##
##l1=[[13,9.5],[3,6.9],[10,5.6]]
##l2=[[14,8.5],[6,7.4],[6,9.6]]


emiA=EMIX(l1,p,t)
emiB=EMIX(l2,p,t)
if emiA>emiB:
    print('B')
else:
    print('A')



