import turtle

def rule(s):
    if s=='F':
        return 'F-G+F+G-F'
    elif s=='G':
        return 'GG'
    else:
        return s


n=0
lim=4
def rec(s):
    global n
    n+=1
    temp = ''
    for i in s:
        temp=temp+rule(i)
    print(temp)
    s = temp
    if n>=lim:
        return s
    return(rec(s))

def draw(s):
    turtle.speed(0)
    turtle.ht()
    for i in s:
        if i=='F' or i=='G':
            turtle.forward(10)
        elif i=='+':
            turtle.left(120)
        elif i=='-':
            turtle.right(120)


s = 'F-G-G'
s=rec(s)
print(s)
draw(s)



 
