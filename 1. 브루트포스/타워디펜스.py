from itertools import combinations
def enemy_go(enemy_map):
    enemy_map.insert(0,[0]*len(enemy_map[0]))
    enemy_map.pop(-1)
def get_archer_target(archer_pos,enemy_map,dist):
    for d in range(dist):
        for i,x in enumerate(range(max(0,archer_pos-d),min(len(enemy_map[0]),archer_pos+d+1))):
            y_pos = (d-abs(archer_pos-x)+1)
            if y_pos <= len(enemy_map):
                if enemy_map[-y_pos][x] == 1:
                    return -y_pos,x
                    
def attack(enemy_map,archer_placement,dist):
    kill = 0
    enemy_to_kill = []
    for archer in archer_placement:
        enemy = get_archer_target(archer,enemy_map,dist)
        if enemy != None:
            enemy_to_kill.append(enemy)
    for enemy_pos in enemy_to_kill:
        if enemy_map[enemy_pos[0]][enemy_pos[1]] == 1:
            enemy_map[enemy_pos[0]][enemy_pos[1]] = 0
            kill += 1
    return kill
def get_kill_by_placement(enemy_map,placement,dist):
    kill = 0
    #print(enemy_map,'\n')
    for i in range(len(enemy_map)):
        kill += attack(enemy_map,placement,dist)
        enemy_go(enemy_map)
        #print(enemy_map,'\n')
    return kill
def get_max_kill(enemy_map,dist):
    max_kill = 0
    placements = combinations(range(len(enemy_map[0])),3)
    for placement in placements:
        max_kill = max(max_kill,get_kill_by_placement(copy_map(enemy_map),placement,dist))
    return max_kill
def copy_map(enemy_map):
    new_map = []
    for row in enemy_map:
        new_map.append(row[:])
    return new_map
N,M,D = tuple(map(int,input().split()))
enemy_map = []
for i in range(N):
    enemy_map.append(list(map(int,input().split())))

print(get_max_kill(enemy_map,D))
