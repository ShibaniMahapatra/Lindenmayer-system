import turtle

def rule(s):
    if s=='F':
        return 'F+F-F-F+F'
    else:
        return s


n=0
lim=2
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
        if i=='F':
            turtle.forward(10)
        elif i=='+':
            turtle.left(90)
        elif i=='-':
            turtle.right(90)


s = 'F'
s=rec(s)
print(s)
draw(s)



 
