a = list(map(int,input().split(' ')))

b = list(map(int,input().split(' ')))
arr=[]
Alice = 0
Bob = 0

for i in range(0,len(a)):
    if a[i]>b[i]:
        Alice = Alice+1
    if a[i]<b[i]:
        Bob =Bob +1
    if a[i]==b[i]:
        continue
            
   
    
arr.append(Alice)
arr.append(Bob)

print(*arr)