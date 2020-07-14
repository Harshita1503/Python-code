a=lambda:(map(int,input().split()))
s,d=a()
c=0
l=list(a())
 
print(sum(v>=max(1,l[d-1])for v in l))
