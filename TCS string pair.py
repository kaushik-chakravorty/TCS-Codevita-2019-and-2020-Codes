from itertools import combinations
from num2words import num2words
def extract(x):
    x=x.split()
    for i in range(len(x)):
        x[i]=int(x[i])
    return x
        

def result(a,d):
    lcomb=[]
    count=0
    comb=combinations(a,2)
    for i in comb:
        lcomb.append(i)
    if len(lcomb)<=10**3:
        for i in range(len(lcomb)):
            if sum(lcomb[i])==d:
                count+=1
    return count

d={'zero': 2, 'one': 2, 'two': 1, 'three': 2, 'four': 2, 'five': 2, 'six': 1, 'seven': 2, 'eight': 2, 'nine': 2, 'ten': 1, 'eleven': 3, 'twelve': 2, 'thirteen': 3, 'fourteen': 4, 'fifteen': 3, 'sixteen': 3, 'seventeen': 4, 'eighteen': 4, 'nineteen': 4, 'twenty': 1, 'twenty-one': 3, 'twenty-two': 2, 'twenty-three': 3, 'twenty-four': 3, 'twenty-five': 3, 'twenty-six': 2, 'twenty-seven': 3, 'twenty-eight': 3, 'twenty-nine': 3, 'thirty': 1, 'thirty-one': 3, 'thirty-two': 2, 'thirty-three': 3, 'thirty-four': 3, 'thirty-five': 3, 'thirty-six': 2, 'thirty-seven': 3, 'thirty-eight': 3, 'thirty-nine': 3, 'forty': 1, 'forty-one': 3, 'forty-two': 2, 'forty-three': 3, 'forty-four': 3, 'forty-five': 3, 'forty-six': 2, 'forty-seven': 3, 'forty-eight': 3, 'forty-nine': 3, 'fifty': 1, 'fifty-one': 3, 'fifty-two': 2, 'fifty-three': 3, 'fifty-four': 3, 'fifty-five': 3, 'fifty-six': 2, 'fifty-seven': 3, 'fifty-eight': 3, 'fifty-nine': 3, 'sixty': 1, 'sixty-one': 3, 'sixty-two': 2, 'sixty-three': 3, 'sixty-four': 3, 'sixty-five': 3, 'sixty-six': 2, 'sixty-seven': 3, 'sixty-eight': 3, 'sixty-nine': 3, 'seventy': 2, 'seventy-one': 4, 'seventy-two': 3, 'seventy-three': 4, 'seventy-four': 4, 'seventy-five': 4, 'seventy-six': 3, 'seventy-seven': 4, 'seventy-eight': 4, 'seventy-nine': 4, 'eighty': 2, 'eighty-one': 4, 'eighty-two': 3, 'eighty-three': 4, 'eighty-four': 4, 'eighty-five': 4, 'eighty-six': 3, 'eighty-seven': 4, 'eighty-eight': 4, 'eighty-nine': 4, 'ninety': 2, 'ninety-one': 4, 'ninety-two': 3, 'ninety-three': 4, 'ninety-four': 4, 'ninety-five': 4, 'ninety-six': 3, 'ninety-seven': 4, 'ninety-eight': 4, 'ninety-nine': 4, 'hundred': 2}
    
lword=[]
N=int(input())
x=input()
x=extract(x)
D=0
for i in range(len(x)):
    lword.append(num2words(x[i]))

for i in lword:
    if i in d:
        D=D+d[i]
        
        
count=result(x,D)
if count>100:
    print('greater 100')
else:
    print(num2words(count))
