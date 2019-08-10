class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('爹的f1')
class OldboyTeacher(OldboyPeople):
    def change_score(self):
        print('teacher %s is changing score' %self.name)

    def f1(self):
        print('儿子的f1')

tea1 = OldboyTeacher('egon', 18, 'male')
tea1.change_score()