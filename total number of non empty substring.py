value="abcd"
count=0
for i in range (0,len(value)):
    for j in range(i,len(value)):
       # print(value[i:j+1])
        count+=1
print(count)