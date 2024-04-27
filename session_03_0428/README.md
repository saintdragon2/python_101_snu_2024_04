# 2번째 시간
- 지난 과제 리뷰 (가위바위보)
- 문자열 정리하기
- dictionary 
- 클래스 복습
- 파일 읽고 쓰기
- 라이브러리 사용하기 (pandas)
- 가상환경


## 가위바위보 게임
```python
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
```

## 문자열 정리하기
### strip
`문자열.strip()`을 이용하면 문자열 앞 뒤의 공백이나 줄바꿈, 탭 등을 벗겨낼 수 있다. 
```python
a = '  앞 뒤에 공백이 있다.   '
b = '\t앞에는 탭이, 뒤에는 줄바꿈이 있다.\n'

print(a)
print(b)
print('-----------STRIP-----------')
print(a.strip())
print(b.strip())
print('----------DONE---------------')
```

### split
`문자열.split(나누고싶은기준이되는구분자)`를 사용해 문자열을 잘라 리스트로 만들 수 있다. 
```python
a = '방시혁;CEO;HIVE'
b = '빈칸이 중간에 있으면?'

print(a)
print(b)
print('-----' * 10)
print('a.split()테스트\t:', a.split())
print('a.split(";")테스트\t:', a.split(';'))
print('b.split()테스트\t:', b.split())
```

### .join
```python
a = ['문자열을', '합칠 때는', '.join()을', '쓰면 된다.']
print(type(a))

b = '_'.join(a)
print(b)
print(type(b))

```

## dictionary 복습
```python
ent_dict = {}
ent_dict['HIVE'] = ['방시혁', 'RM', '뷔', '정국']
ent_dict['SM'] = ['카리나', '보아']

print(ent_dict.keys())
print(ent_dict.values())
print('-----' * 10)

for k, v in ent_dict.items():
    print(k)
    for p in v:
        print('\t', p)
    print('-----' * 10)
    
print('HIVE' in ent_dict)
print('JYP' in ent_dict)
print('카리나' in ent_dict)

```

## 클래스 복습
```python
class EntCompay:
    def __init__(self, name):
        self.name = name
        self.people = []
        
    def people_count(self):
        return len(self.people)
    
    def get_people_by_role(self, role):
        people = []
        for person in self.people:
            if person[1] == role:
                people.append(person[0])
        return people
    
        
sm = EntCompay('SM')
sm.people.append(['보아', '가수'])
sm.people.append(['카리나', '가수'])
sm.people.append(['장철혁', 'CEO'])

print(sm.people_count())
print(sm.get_people_by_role('CEO'))

hive = EntCompay('HIVE')
hive.people.append(['방시혁', 'CEO'])
hive.people.append(['RM', '가수'])
hive.people.append(['뷔', '가수'])
hive.people.append(['정국', '가수'])

print(hive.people_count())
print(hive.get_people_by_role('가수'))
```

## 파일 읽고 쓰기

아래와 같은 파일이 있다고 가정하자. 파일명은 `ent_business.txt`이다. 
```
방시혁;CEO;HIVE
박진영;CEO;JYP
유희열;CEO;Antena
유재석;MC;Antena
```

### open, close 사용하는 방법
`open(파일경로, 읽는 방법)`으로 읽는다. "읽는 방법"은 여러가지가 있는데, 나는 거의 세가지만 쓴다. 

|구분|내용|
|-|-|
|r|읽기전용|
|w|쓰기|
|a|뒤에 이어쓰기|



### open & close
```python
f = open('./session_03_0428/data/ent_business.txt', 'r')

for line in f.readlines():
    print(line)

f.close()
```
아래와 같이 출력된다. 
```
방시혁;CEO;HIVE

박진영;CEO;JYP

유희열;CEO;Antena

유재석;MC;Antena
```

왜 한 줄씩 띄어서 출력될까? `f.readlines()`로 읽었을 때, 각 줄 끝에 줄바꿈이 있기 때문에 줄바꿈(`\n`)까지 출력하고 print 특성상 줄바꿈을 하기 때문이다. 

`.strip()`으로 정리하자. `.strip()`은 문자열에서 앞 뒤, 공백이나 줄바꿈 같은 기호를 지워주는 역할이다. 
```python
f = open('./session_03_0428/data/ent_business.txt', 'r')

for line in f.readlines():
    print(line.strip())

f.close()
```
세미콜론(;)으로 구분을 하고 싶다. `문자열.split(자르는구분자)`를 쓰면 된다. 
```python
f = open('./session_03_0428/data/ent_business.txt', 'r')

for line in f.readlines():
    values = line.strip().split(';')
    print(values, type(values))

f.close()
```
`split`을 사용해 리스트 형태로 분리했다. 
```
['방시혁', 'CEO', 'HIVE'] <class 'list'>
['박진영', 'CEO', 'JYP'] <class 'list'>
['유희열', 'CEO', 'Antena'] <class 'list'>
['유재석', 'MC', 'Antena'] <class 'list'>
```

### 여태 배운걸 모두 합치면!
```python
class EntCompany:
    def __init__(self, name):
        self.name = name
        self.people = []
        
    def people_count(self):
        return len(self.people)
    
    def get_people_by_role(self, role):
        people = []
        for person in self.people:
            if person[1] == role:
                people.append(person[0])
        return people
    

ent_dict = {}



f = open('./session_03_0428/data/ent_business.txt', 'r')

for line in f.readlines():
    values = line.strip().split(';')
    
    name = values[0]
    role = values[1]
    company = values[2]
    
    if company not in ent_dict:
        ent_dict[company] = EntCompany(company)
    ent_dict[company].people.append([name, role])
    

f.close()



for k, v in ent_dict.items():
    print(k)
    for p in v.people:
        print(p)
    print('-----' * 10)
    
lsy = EntCompany('LSY')
lsy.people.append(['이성용', 'CEO'])
lsy.people.append(['아이유', '가수'])
ent_dict['LSY'] = lsy

    
f = open('./session_03_0428/data/ent_business_edited.txt', 'w')
f.write('이름;역할;회사명\n')
for k, v in ent_dict.items():
    for p in v.people:
        line = ';'.join([p[0], p[1], k])
        f.write(line + '\n')
f.close()
```

### with로 하는 방법
`open()`, `close()`로 하는 것과 다를게 없지만 깜빡 잊고 close를 안한다든지, 중간에 프로그램이 죽었는데 열었던 파일 처리가 잘 안된다든지 하는 문제를 없애기 위해 `with`를 씀 
```python
class EntCompany:
    def __init__(self, name):
        self.name = name
        self.people = []
        
    def people_count(self):
        return len(self.people)
    
    def get_people_by_role(self, role):
        people = []
        for person in self.people:
            if person[1] == role:
                people.append(person[0])
        return people
    

ent_dict = {}



# f = open('./session_03_0428/data/ent_business.txt', 'r')
with open('./session_03_0428/data/ent_business.txt', 'r') as f:
    for line in f.readlines():
        values = line.strip().split(';')
        
        name = values[0]
        role = values[1]
        company = values[2]
        
        if company not in ent_dict:
            ent_dict[company] = EntCompany(company)
        ent_dict[company].people.append([name, role])
    

# f.close()



for k, v in ent_dict.items():
    print(k)
    for p in v.people:
        print(p)
    print('-----' * 10)
    
lsy = EntCompany('LSY')
lsy.people.append(['이성용', 'CEO'])
lsy.people.append(['아이유', '가수'])
ent_dict['LSY'] = lsy

    
# f = open('./session_03_0428/data/ent_business_edited.txt', 'w')
with open('./session_03_0428/data/ent_business_edited.txt', 'w') as f:
    f.write('이름;역할;회사명\n')
    for k, v in ent_dict.items():
        for p in v.people:
            line = ';'.join([p[0], p[1], k])
            f.write(line + '\n')
# f.close()
```

## from import
프로그램이 커지는데 모든 내용을 한 .py 파일에 다 쓸 순 없다. 
- 파일이 무한정 길어지고, 
- 공동 작업도 어렵다. 

```python
# ent_bunisess.py
class EntCompany:
    def __init__(self, name):
        self.name = name
        self.people = []
        
    def people_count(self):
        return len(self.people)
    
    def get_people_by_role(self, role):
        people = []
        for person in self.people:
            if person[1] == role:
                people.append(person[0])
        return people
    
```
이렇게 만들어놓고, 다른 파이썬 파일에서 `from import`로 불러올 수 있다. 

```python 
from ent_business import EntCompany


lsy = EntCompany('LSY')
lsy.people.append(['이성용', 'CEO'])
lsy.people.append(['아이유', '가수'])

print(lsy.people_count())
```