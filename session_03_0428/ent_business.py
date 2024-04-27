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
    