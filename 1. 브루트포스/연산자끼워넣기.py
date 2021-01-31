from itertools import combinations


def compare_all_case(nums,opts,case,max_val,min_val):
    if len(opts) == 0:
        val = value_bycase(nums,case[1:])
        return max(max_val,val), min(min_val,val)
    else:
        opt = opts[0]
        selects = list(combinations(case[0],opt))
        for select in selects:
            remain = list(filter(lambda x : x not in select, case[0]))
            new_case = [remain] + case[1:] + [list(select)]
            vals = compare_all_case(nums,opts[1:],new_case,max_val,min_val)
            max_val,min_val = max(max_val,vals[0]), min(min_val,vals[1])
        return max_val, min_val
def value_bycase(nums,case):
    result = nums[0]
    for i in range(len(nums)-1):
        if i in case[0]: 
            result += nums[i+1]
        elif i in case[1]: 
            result -= nums[i+1]
        elif i in case[2]: 
            result *= nums[i+1]
        else: 
            if result >= 0:
                result //= nums[i+1] 
            else:
                result = -(-result// nums[i+1])
    return result
 
input()
nums = list(map(int, input().split()))
opts = list(map(int, input().split()))
space = list(range(len(nums)-1))
answer = compare_all_case(nums,opts,[space],-1000000001,1000000001)
print(int(answer[0]))
print(int(answer[1]))
