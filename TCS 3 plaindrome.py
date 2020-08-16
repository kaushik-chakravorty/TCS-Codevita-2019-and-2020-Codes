lindex=[]
def palindrome(x):
    l=[]
    if x=='':
        exit
    else:
        
        a=x[0]
        for j in range(1,len(x)):
            if x[j]==a:
                l=x[:j+1]
                print(l)
                break
            
##            else:
##                print('impossible')

       
    if l==l[::-1]:
        lindex.append(j)
        palindrome(x[j+1:])
    else:
        palindrome(x[1:])##return it to original function to check for repetition. the function won't have the name palindrome

    


#y=input()
y='nayannamantenet'

if y[0]==y[1]:
    print('yo')


else:
    palindrome(y)
palindrome(y)
print('the three palindromes are', x[:lindex[0]+1],x[lindex[0]+1:lindex[1]+1,lindex[1]+1,lindex[2]+1])

