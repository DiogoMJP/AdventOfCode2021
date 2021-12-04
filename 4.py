# Parte 1
t=open("input.txt","r").readlines();n=[int(x)for x in t[0].split(",")]
b=[];t=t[1:];del t[0::6]
for l in range(len(t)):
    if l%5==0:b+=[[]]
    b[-1]+=[[int(x)for x in t[l].split(" ") if x != ""]]
for j in n:
    for t in b:
        for l in t:
            for x in l:
                if x == j:
                    i=l.index(j)
                    l[i]=" "
                    if l == [" "]*5 or [t[h][i] for h in range(5)] == [" "]*5:
                        print(j * sum([sum([n for n in l if n!=" "]) for l in t]))
                        break
            else:continue
            break
        else:continue
        break
    else:continue
    break

# Parte 2
t=open("input.txt","r").readlines();n=[int(x)for x in t[0].split(",")]
b=[];t=t[1:];del t[0::6]
for l in range(len(t)):
    if l%5==0:b+=[[]]
    b[-1]+=[[int(x)for x in t[l].split(" ") if x != ""]]
for j in n:
    win=[]
    for t in b:
        for l in t:
            for x in l:
                if x == j:
                    i=l.index(j)
                    l[i]=" "
                    if l == [" "]*5 or [t[h][i] for h in range(5)] == [" "]*5:
                        print(j * sum([sum([n for n in l if n!=" "]) for l in t]))
                        win+=[t]
    if win != []:
        for t in win:b.remove(t)
