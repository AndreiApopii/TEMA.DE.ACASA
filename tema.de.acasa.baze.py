def cifra_maxima(a):
    max=0
    while a>0:
        r=a%10
        a/=10
        if r>max:
            max=r
    return max

def ver_bazei(a,b):
    elem=cifra_maxima(a)
    if elem<(b):
        return True
    else:
        return False
    
def baza_necunoscuta_in_baza_zece(a,b):
        x=0
        y=0
        while a>0:
            r=a%10
            k=r*(b**x)
            a//=10
            y=y+k
            x=x+1
        return y

def suma_2_baze_zece(p,q,b):
    aa=baza_necunoscuta_in_baza_zece(p,b)
    bb=baza_necunoscuta_in_baza_zece(q,b)
    c=aa+bb
    return c

def convertirea_din_baza_10_in_alta_adunarea(a,q,b):
    sum=suma_2_baze_zece(p,q,b)
    list=[]
    while sum>0:
        nr=sum//b
        k=sum-(b*nr)
        list.append(k)
        sum=nr
    br=reversed(list)
    finish=''.join(map(str,br))
    return print("Suma numerelor",xx,"si",yy,"in baza",zz,"este:",finish,'.')

def diferenta_2_baze_zece(a,q,b):
    aa=baza_necunoscuta_in_baza_zece(p,b)
    bb=baza_necunoscuta_in_baza_zece(q,b)
    if aa>bb:
        c=aa-bb
        return c
    elif bb>aa:
        c=bb-aa
        return c

def convertirea_din_baza_10_in_alta_scaderea(p,q,b):
    dif=diferenta_2_baze_zece(p,q,b)
    list=[]
    while dif>0:
        nr=dif//b
        k=dif-(b*nr)
        list.append(k)
        dif=nr
    br=reversed(list)
    finish=''.join(map(str,br))
    return print("Diferenta numerelor",xx,"si",yy,"in baza",zz,"este:",finish,'.')

#4
def inmultirea_2_baze_10(a,q,b):
    aa=baza_necunoscuta_in_baza_zece(p,b)
    bb=baza_necunoscuta_in_baza_zece(q,b)
    c=aa*bb
    return c

def convertirea_din_baza_10_in_alta_inmultirea(p,q,b):
    inm=inmultirea_2_baze_10(p,q,b)
    list=[]
    while inm>0:
        nr=inm//b
        k=inm-(b*nr)
        list.append(k)
        inm=nr
    br=reversed(list)
    finish=''.join(map(str,br))
    return print("Inmultirea numerelor",xx,"si",yy,"in baza",zz,"este:",finish,'.')

import random 
xx=random.randint(1,999)
yy=random.randint(1,999)
zz=random.randint(2,9)

print("Primul nr:",xx)
print("Al doilea nr:",yy)
print("Baza numerelor:",zz)

if (zz>1) and (zz<10):
    print("Rezultatul verificarii bazei numarului",xx,"este:",ver_bazei(xx,zz))
    print("Rezultatul verificarii bazei numarului",yy,"este:",ver_bazei(yy,zz))
    if ver_bazei(xx,zz) and ver_bazei(yy,zz) :
        convertirea_din_baza_10_in_alta_adunarea(xx,yy,zz)
        convertirea_din_baza_10_in_alta_scaderea(xx,yy,zz)
        convertirea_din_baza_10_in_alta_inmultirea(xx,yy,zz)