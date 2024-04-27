import random

rsp = {
    0: '가위', 1: '바위', 2: '보'
}

# n판3선승제(유저가 3번 이기면 게임종료)
# 0, 1, 2 대신 다른 값을 입력하면 0, 1, 2 중에 하나를 다시 넣도록 함

def judge(user_no, computer_no):
    if abs(user_no - computer_no) <= 1: # 컴퓨터와 유저의 차이(절대값)가 1 이하이면 값 단순비교
        if user_no < computer_no:
            result = 1 #'컴퓨터가 이겼습니다.'
        elif user_no > computer_no:
            result = -1 #'사용자가 이겼습니다.'
        else:
            result = 0 #"비겼습니다"
    else:                               # (가위, 보)로써 값 차이가 2이면 앞의 경우와 반대됨
        if user_no < computer_no:
            result = -1 #'사용자가 이겼습니다.'
        elif user_no > computer_no:
            result = 1 #'컴퓨터가 이겼습니다.'
    return result

# 게임 시작
print('-----' * 10)
print("3판을 먼저 이기면 최종승리합니다.") # n판3선승제
print()

user_win = 0 # 사용자가 이긴 횟수
com_win = 0  # 컴퓨터가 이긴 횟수
i = 1        # 승률을 계산하기 위한 전체횟수

while user_win <= 2 and com_win <= 2: #3판 이기는 것이 조건이므로 while문 사용

    print(i, "번째 판") # i번째 판
 
    # 컴퓨터가 낸 가위바위보
    computer_choice = random.randint(0, 2)
    computer = rsp[computer_choice]

    # 유저가 낸 가위바위보
    user_input = input('가위는 0, 바위는 1, 보는 2를 내세요:')
    user_input = user_input.strip()
    while user_input not in ['0', '1', '2']:
        print('0, 1, 2 중에 하나를 입력하세요')
        user_input = input('가위는 0, 바위는 1, 보는 2를 내세요:')
    user_input = int(user_input)
    
    # while user_input:
    #     try: # 정수가 아닌 값 입력하면 int 구문에서 ValueError 떠서 try, except 사용
    #         user_input = int(user_input)
    #         if int(user_input in rsp) != 1: # 0, 1, 2, 아닌 정수값을 입력할 때를 대비함
    #             print('0, 1, 2 중에 하나를 입력하세요')
    #             user_input = input('가위는 0, 바위는 1, 보는 2를 내세요:')
    #         else: 
    #             break
    #     except ValueError:          
    #         print('정수를 입력하세요')
    #         user_input = input('가위는 0, 바위는 1, 보는 2를 내세요:') 
    user = rsp[user_input]

    # 가위바위보 산출
    print()
    print('user:', user)
    print('computer:', computer)
    print()

    # 승부결과
    result = judge(user_input, computer_choice)

    if result == 1:
        print('결과: 컴퓨터가 이겼습니다.')
        com_win = com_win + 1
        i = i + 1
    elif result == -1:
        print('결과: 사용자가 이겼습니다')
        user_win = user_win + 1
        i = i + 1
    else:
        print('결과: 비겼습니다')    
        i = i + 1

    print('사용자승리:', '☆ ' * user_win)
    print('컴퓨터승리:', '★ ' * com_win)
    print('-----' * 10)

# 사용자나 컴퓨터가 이긴 회수가 3이 되면 게임 종료
print("게임이 끝났습니다")

if user_win == 3: # 사용자가 이긴 경우
    print("최종결과: 사용자 승리")
    print("승률:", user_win/(i-1)*100, '%')
else:             # 컴퓨터가 이긴 경우
    print("최종결과: 컴퓨터 승리")
    print("승률:", com_win/(i-1)*100, '%')

# 문제점 : input 시에 아무것도 입력 안하면 오류가 뜸