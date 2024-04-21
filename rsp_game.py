import random

rsp = {
    0: '가위', 1: '바위', 2: '보',
}

def judge(user_no, computer_no):
    if user_no < computer_no:
        result = '컴퓨터가 이겼습니다.'
    elif user_no > computer_no:
        result = '사용자가 이겼습니다.'
    else:
        result = '비겼습니다.'
    return result


for i in range(10):
    print('ROUND ', i, '---------------------------')
    computer_choice = random.randint(0, 2)
    computer = rsp[computer_choice]

    user_input = input('가위는 0, 바위는 1, 보는 2를 내세요: ')
    user_input = int(user_input)
    user = rsp[user_input]
    print('user:', user)
    print('computer:', computer)

    r = judge(user_input, computer_choice)
    print(r)

# 가위바위보 게임을 업그레이드하기
    # 버그 없애기 (보 내면 현재 무적)
    # 승률 계산하기
# 가위바위보가 재미없다면, 다른 게임 만들기 (up & down, hangman, )
    


    
    # if computer_choice == 0:
    #     computer = '가위'
    # elif computer_choice== 1:
    #     computer = '바위'
    # elif computer_choice == 2:
    #     computer = '보'
    # else:
    #     print('something went wrong')
    