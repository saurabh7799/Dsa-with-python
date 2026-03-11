def armstrong(n):
    num=n
    total=0
    nod=len(str(n))
    while num>0:
        id=num%10
        total+=id**nod
        num=num//10
    return n==total
print(armstrong(153))