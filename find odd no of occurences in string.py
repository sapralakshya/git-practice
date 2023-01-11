value="geekforgeeks is best for geeks"
dict={}
list_dict=[]
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
for i in dict:
    if dict[i]%2!=0:
        list_dict.append(i)
print(list_dict)
