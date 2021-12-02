# Parte 1
depth=0;horiz=0
for x in[x.split(" ")for x in open("input.txt", "r").readlines()]:
    if x[0]=="forward":horiz+=int(x[1])
    if x[0]=="down":depth+=int(x[1])
    if x[0]=="up":depth-=int(x[1])
print(horiz*depth)

# Parte 2
depth=0;horiz=0;aim=0
for x in[x.split(" ")for x in open("input.txt", "r").readlines()]:
    if x[0]=="forward":horiz+=int(x[1]);depth+=aim*int(x[1])
    if x[0]=="down":aim+=int(x[1])
    if x[0]=="up":aim-=int(x[1])
print(horiz*depth)
