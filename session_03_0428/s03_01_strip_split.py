a = '      앞 뒤에 공백이 있다.      '
b = '\t앞에는 탭이, 뒤에는 줄바꿈이 있다.\n'

print(a)
print(b)
print('-----------STRIP-----------')
print(a.strip())
print(b.strip())
print('----------DONE---------------')



a = '방시혁;CEO;HIVE'
b = '빈칸이 중간에 있으면?'

print(a)
print(b)
print('-----' * 10)
print('a.split()테스트\t:', a.split())
print('a.split(";")테스트\t:', a.split(';'))
print('b.split()테스트\t:', b.split())

print('-----' * 10)

a = ['문자열을', '합칠 때는', '.join()을', '쓰면 된다.']
print(type(a))

b = '_'.join(a)
print(b)
print(type(b))