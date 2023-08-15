s = "yooyyo 12s k"
l = s.split()
z= 0
k = ''
for i in l:
    try:
       int(i[0])
       l[z] = k + i

    except ValueError:
        l[z] = k +i.title()
    z +=1
print(l)

