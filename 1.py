#Parte 1
i=[int(x)for x in open("input.txt","r").readlines()];print(sum([i[x]>i[x-1]for x in range(1,len(i))]))

# Parte 2
i=[int(x)for x in open("input.txt","r").readlines()];j=[i[x-2]+i[x-1]+i[x]for x in range(2,len(i))];print(sum([j[x]>j[x-1]for x in range(1,len(j))]))
