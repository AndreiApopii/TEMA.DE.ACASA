a=int(input('a='))
b=int(input('b='))
def suma(x,y):
    s=x+y
    return s

def produs(x,y):
    p=x*y
    return p

def aritmetica(x,y):
    ma=(x+y)/2
    return ma

def cel_mai_mare_div_comun(x,y):
    c=[]
    d=[]
    for i in range(1,x+1):
        if (x%i==0):
            c.append(i)
    for j in range (1,y+1):
        if (y%i==0):
            d.append(j)
    w=set(c).intersection(d)
    z=max(w)
    return w

def c_mai_mic_mult_comun(x,y):
    if x>y:
        multiplu=x
    elif y>x:
        multiplu=y
    else:
        multiplu=x
    while True:
        if ((multiplu%x==0)and(multiplu%y==0)):
            cel_mai_mic_m=multiplu
            break
        multiplu =multiplu+1
    return multiplu

def min(x,y):
    if x<y:
        return print('Numarul minim este: ',a)
    else:
        return print('Numarul minim este: ',b)

def suma_nedefinita(x,y):
    c=a+b
    return c

def produs_nedefinit(x,y):
    c=a*b
    return c
print(a,'+',b,'=',suma(a,b))
print(a,'*',b,'=',produs(a,b))
print('media aritmetica=',aritmetica(a,b))
print('cel mai mare divizor comun este=',cel_mai_mare_div_comun(a,b))
print("Cel mai mic multiplu comun este=",cel_mai_mic_mult_comun(a,b))
print('a+b=',suma_nedefinita(a,b))
print('a*b=',produs_nedefinit(a,b))


