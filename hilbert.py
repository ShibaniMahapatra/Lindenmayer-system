#   Fractals using L-system
#   Authour:Alan Richmond, Python3.codes
#   https://en.wikipedia.org/wiki/L-system

from turtle import*
#from random import gauss

t=30                    # angle of branches
d=10                    # length of branches
n=5                     # max depth of recursion

X="F-[[X]+X]+F[+FX]-X"  # Lindenmayer system
F="F"

stack=[]

def x(n):
    if n>0: L(X,n)
    else:   dot(6,'green')
    
def f(n):
    if n>0: L(F,n)
    
def L(s,n):
    speed(0)
    pensize(n*2)
    for c in s:

#        if   c=='-':    lt(gauss(t,t))
#        elif c=='+':    rt(gauss(t,t))
        if   c=='-':    lt(t)
        elif c=='+':    rt(t)
        elif c=='X':    x(n-1)
        elif c=='F':    f(n-1);fd(d)
        elif c=='[':    stack.append((pos(),heading(),n))
        elif c==']': 
            ((i,j),h,p)=stack.pop()
            penup()
            goto(i,j)
            seth(h)
            pensize(p)
            pendown()

penup()
goto(0,-200)
pendown()
seth(90)
color('brown','green')
x(n)
