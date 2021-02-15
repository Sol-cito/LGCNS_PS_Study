import sys
def check(dict,txt):
    txt = txt.strip()
    isExist = True
    now = dict
    for t in txt:
        if not t in now:
            isExist = False
            now[t] = {}
            if 'f' in now:
                return True
        now = now[t]
    now['f'] = {}
    return isExist
 
for t in range(int(sys.stdin.readline())):
    trie = {}
    valid = True
    for i in range(int(sys.stdin.readline())):
        if valid:
            valid = not check(trie,sys.stdin.readline())  
        else:
            sys.stdin.readline()
    print("YES" if valid else "NO")
