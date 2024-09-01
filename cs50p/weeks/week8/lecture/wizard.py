class Wizard:
    def __init__(self, name):
        self.name = name

class Prof(Wizard):
    def __init__(self, subject, name):
        super().__init__(name)
        self.subject = subject

class Student(Wizard):
    def __init__(self, house, name):
        super().__init__(name)
        self.house = house


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Prof("Svreus", "Defence Against the dark arts")