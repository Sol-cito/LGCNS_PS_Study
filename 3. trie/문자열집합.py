n,m = list(map(int,input().split()))
S = set(map(lambda x: input(), range(n)))
srch = sum(list(map(lambda x : 1 if input() in S else 0, range(m))))
print(srch)
