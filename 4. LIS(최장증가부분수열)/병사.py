n=int(input())
arr=list(map(int,input().split()))[::-1]
max_len=[]
for i in range(n): 
    max_len.append(1)
    for j in range(i): 
        if arr[j]<arr[i]:
            max_len[i]=max(max_len[j]+1,max_len[i]) 
print(n-max(max_len))
