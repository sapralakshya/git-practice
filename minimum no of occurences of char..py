value="mmmaacogggg"
dict={}
for i in value:
    dict[i]=None
for i in range (0,len(value)):
    a=1
    if dict[value[i]]==None:
        for j in range(i+1,len(value)):
            if value[i]==value[j]:
                a+=1
        dict[value[i]]=a
print(dict)
temp=dict[value[0]]
key=None

for i in range(1,len(value)):
    if dict[value[i]]<=temp:
        temp=dict[value[i]]
        key=value[i]
print(key)



