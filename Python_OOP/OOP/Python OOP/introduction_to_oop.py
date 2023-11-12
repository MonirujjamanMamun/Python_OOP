class School:
    def __init__(self, School_name, student, teacher, address) -> None:
        self.School_name = School_name
        self.student = student
        self.teacher = teacher
        self.address = address


class Teacher(School):
    def __init__(self, School_name, id, name, age, level_teacher) -> None:
        super().__init__(School_name)
        self.id = id
        self.name = name
        self.age = age
        self.level_teacher = level_teacher

    def details(self):
        print(
            f'My name is {self.name}, I am a class Teacher of {self.level_teacher}')


class Students(School, Teacher):
    def __init__(self, School_name, teacher, id, name) -> None:
        super().__init__(School_name, teacher)
        self.id = id
        self.name = name

    def details(self):
        print(
            f'I am a student of {self.School_name} and my name is {self.name}, my class teacher name is {self.level_teacher}.')
