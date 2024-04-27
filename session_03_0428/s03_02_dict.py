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