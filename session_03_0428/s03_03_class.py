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
    
        
sm = EntCompany('SM')
sm.people.append(['보아', '가수'])
sm.people.append(['카리나', '가수'])
sm.people.append(['장철혁', 'CEO'])

print(sm.people_count())
print(sm.get_people_by_role('CEO'))

hive = EntCompany('HIVE')
hive.people.append(['방시혁', 'CEO'])
hive.people.append(['RM', '가수'])
hive.people.append(['뷔', '가수'])
hive.people.append(['정국', '가수'])

print(hive.people_count())
print(hive.get_people_by_role('가수'))