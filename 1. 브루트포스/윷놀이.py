


def get_score(id):
    if id in score_rule:
        return score_rule[id]
    elif id == 21:
        return 0
    else:
        return id*2
def go_by_dice(player,dice,pos):
    for i in range(dice):
        if i == 0 and pos in warp:
            pos = warp[pos]
        elif pos == 21:
            return 21
        elif pos in path:
            pos = path[pos]
        else:
            pos += 1
    return -1 if (pos in player and pos != 21) else pos
def get_max(player,dice_list,max_score):
    if len(dice_list) == 0:
        return max_score
    else:
        candidate = []
        for i in range(4):
            new_pos =  go_by_dice(player,dice_list[0],player[i])
            if new_pos > 0:
                score = get_max(player[:i] + [new_pos] + player[i+1:],dice_list[1:],max_score+get_score(new_pos)) 
                candidate.append(score)
        return max_score if len(candidate)==0 else max(candidate)
warp = { 5 : 22, 10 : 28, 15:30}
path = {29:25, 32:25, 27:20}
score_rule = {22:13,23:16,24:19,25:25,26:30,27:35,28:22,29:24,30:28,31:27,32:26}

dice_predict = list(map(int,input().split()))

player = [0,0,0,0]
print(get_max(player,dice_predict,0))


   
