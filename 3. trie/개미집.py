#개미집
house_data = {}
#입력 값 갯수만큼 돌기
for i in range(int(input())):
    #개미 데이터 입력받음
    ant_data = input().split()
    #현재 선택 노드는 개미집 전체로 시작
    now_dict = house_data
    #맨 앞은 몇개인지 숫자이므로 1부터 길이만큼 돌면서 단어를 받음
    for j in range(1,len(ant_data)):
        #노드가 있으면 그 노드를 선택하고 없으면 하나 만들어서 선택
        if not ant_data[j] in now_dict:
            now_dict[ant_data[j]] = {}
        now_dict = now_dict[ant_data[j]]
#정답처럼 프린트하기
def print_answer(dic,prefix = ''):
    for key in sorted(dic.keys()):
        #딕셔너리 키를 정렬해서 프리픽스와 함께 출력
        print(prefix+key)
        #하위 딕셔너리를 출력
        print_answer(dic[key],'--'+prefix)
print_answer(house_data)
