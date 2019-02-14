N,K=list(map(int,input().split()))
f=list(map(int,input().split()))
a=0
summ=0
while a<K:
    summ=summ+f[a]
    a=a+1
print(summ)	
