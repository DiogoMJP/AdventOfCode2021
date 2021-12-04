# Parte 1
t=open("input.txt", "r").readlines();l=len(t[0])-1;epsilon=int("1"*l,base=2)
gamma=int("".join([str(int(sum([int(x[i]) for x in t])>len(t)/2)) for i in range(l)]),base=2);epsilon=epsilon^gamma
print(gamma * epsilon)

# Parte 2
def filter(l,n):
    if len(l)<=1: return l,l
    if (n == len(l[0])): return l,l
    y=sum([int(x[n]) for x in l])/len(l)
    if y < 0.5:
        o2,_=filter([x for x in l.copy() if x[n] == "0"],n+1)
        _,co2=filter([x for x in l.copy() if x[n] == "1"],n+1)
    else:
        o2,_=filter([x for x in l.copy() if x[n] == "1"],n+1)
        _,co2=filter([x for x in l.copy() if x[n] == "0"],n+1)
    return o2,co2
t=[x[:-1] for x in open("input.txt", "r").readlines()[:-1]]+[open("input.txt", "r").readlines()[-1]];l=len(t[0])
o2,co2=filter(t,0)
print(int(o2[0],base=2)*int(co2[0],base=2))
