'''
애초에 복잡도가 O(n)이라 부분합 안 쓰는 게 실제로 더 빠름
'''
def rec(arr):
    if len(arr) == 1:
        return arr,arr[0]
    else:
        half = len(arr)//2
        rec1 = rec(arr[:half])
        rec2 = rec(arr[half:])
        return get_max_sum(arr)
		
def get_max_sum(arr):
	s_idx,f_idx = 0,0
	now_sum, max_sum  = arr[0], arr[0]
	for i in range(1,len(arr)):
		if now_sum + arr[i] < arr[i]:
			s_idx = i
			now_sum = arr[i]
		else:
			now_sum = now_sum + arr[i]
		if max_sum <= now_sum:
			f_idx = i+1
			max_sum = now_sum			
	return arr[:s_idx] + [sum(arr[s_idx:f_idx])] + arr[f_idx:], max_sum
	
for i in range(int(input())):
    _, arr = input(),list(map(int,input().split()))
    print(rec(arr)[-1])

