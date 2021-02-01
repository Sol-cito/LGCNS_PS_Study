def get_messi_len():
    messi_len = [0,5,13]
    while messi_len[-1] <  2**31:
        messi_len.append(messi_len[-1] + messi_len[-2] + 1)
    return messi_len
def get_where(n,m):
    if m == 0:
        return 2,6
    if n < 3:
        return n,m
    else:
        
        if messi_len[n-1] < m:
            return get_where(n-2,m-messi_len[n-1]-1)
        else:
            return get_where(n-1,m)
            
messi_len = get_messi_len()
messi_str = ("Messi", "Messi Gimossi")
n,m = get_where(len(messi_len)-1,int(input()))
answer = messi_str[n-1][m-1]
print("Messi Messi Gimossi" if answer == ' ' else answer)
