def m():
    l = []
    while True:
        k = input(f"Ingrese el elemento {len(l) + 1} de la lista (o presione Enter para terminar): ")
        if k == '':
            break
        l.append(float(k))
    return l

def prm(*args):
    k = []
    for j in range(len(args[0])):
        x = 0
        for i in args:
            x += (i[j])
        k.insert(j, x/len(args))
    return k

def med(a,b,c,d,e):
    q = []
    p = len(a)
    l = p//2
    for i in range(p):
        k = [a[i], b[i], c[i], d[i], e[i]]
        k.sort()
        q.append(k[l])
    return q

def prmx(*args):
    k = []
    for j in range(len(args[0])):
        x = 1
        for i in args:
            x *= (i[j])
        k.insert(j, x**1/(len(args)))
    return k

def ord(*args):
    for i in args:
        for j in range(args):
            k = [i(j)]
        k.sort()
    for i in args:
        print(i)

def ordx(*args):
    for i in args:
        i.sort(reverse=True)
    print("Listas ordenadas de mayor a menor:")
    for i in args:
        print(i)

def mmx(*args):
    k = []
    for i in args:
        l = max(i)**min(i)
        k.append(l)
    return print(k)

def minx(*args):
    for i in args:
     l = min(i)**(1/3)
    return l

if __name__ == "__main__":
    p = m()
    q = m()
    r = m()
    s = m()
    t = m()
    
    z = prm(p, q, r, s, t)
    k = med(p, q, r, s, t)
    l = prmx(p, q, r, s, t)

    print("Promedio", z)
    print("Mediana:", k)
    print("Promedio geométrico:", l)
    
