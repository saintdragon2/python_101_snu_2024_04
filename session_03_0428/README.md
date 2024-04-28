# 2번째 시간
- 지난 과제 리뷰 (가위바위보)
- 문자열 정리하기
- dictionary 
- 클래스 복습
- 파일 읽고 쓰기
- 라이브러리 사용하기 (pandas)
- 가상환경



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