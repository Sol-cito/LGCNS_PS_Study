def get_box_needed(req,own):
    for i in range(len(req)):
        need = req[i] - own[i]
        if need > 0:
            if i == len(req)-1:
                return -1
            own[i+1] -= need * 8
            own[i] += need * 8
        else:
            own[i] = req[i]
            
    return sum(own)

x,y,z = tuple(map(int,input().split()))
own,req = [],[]
for i in range(int(input())):
    key,val = tuple(map(int,input().split()))
    while len(own) < key:
        own.append(0)
    own.append(val)
    size = key
own.reverse()    
count = list(map(lambda s : (x//2**s) * (y//2**s) * (z//2**s),range(size+1)))
count.append(0)
while size >= 0:
    req.append(count[size] - count[size+1] * 8)
    size -= 1
print(get_box_needed(req,own))
