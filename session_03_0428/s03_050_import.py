from ent_business import EntCompany


lsy = EntCompany('LSY')
lsy.people.append(['이성용', 'CEO'])
lsy.people.append(['아이유', '가수'])

print(lsy.people_count())