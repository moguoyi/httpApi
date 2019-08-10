class OldboyPeople:
    school ='oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Oldboyteacher(OldboyPeople):
    def change_score(self):
        print('teacher %s is changing score ' %self.name)

class Oldboystudent(OldboyPeople):
    def choose(self):
        print('student %s choose course'%self.name)

tea1 = Oldboyteacher('egon', 18, 'male')
stu1=Oldboystudent('alex',73,'female')
print(tea1.name,tea1.age,tea1.sex)#egon 18 male
print(stu1.choose())
