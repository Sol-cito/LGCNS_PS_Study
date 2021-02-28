n, m = list(map(int,input().split()))

box = list(map(int, input().split()))
book = list(map(int, input().split()))

box_idx = 0  
book_idx = 0  

while(box_idx < n and book_idx < m): 
    if box[box_idx] >= book[book_idx]:  
        box[box_idx] -= book[book_idx]   
        book_idx += 1     
    else:  
        box_idx += 1     
        
print(sum(box))
