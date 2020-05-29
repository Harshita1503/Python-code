a=str(input())
c=0
for i in range(0,(len(a)-2)):
    for j in range(i+1,(len(a)-1)):
        if a[i]==a[j]:
            c+=1
if (c>0):
    print("ENTER")
else:
    print("DO NOT ENTER")
