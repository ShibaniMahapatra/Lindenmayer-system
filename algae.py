from turtle import*

def rule(s):
    if s=='A':
        return 'AB'
    elif s=='B':
        return 'A'

n=0
lim=5
def rec(s):
    global n
    n+=1
    temp = ''
    for i in s:
        temp=temp+rule(i)
    print(temp)
    s = temp
    if n==lim:
        return s
    return(rec(s))

s = 'A'
s=rec(s)
print(s)
