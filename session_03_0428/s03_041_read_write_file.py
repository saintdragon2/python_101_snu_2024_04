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