from student_data import Student_name

class Devops_student(Student_name):
    def __init__(self, first_name, last_name,prog_lang):
        self.first_name = first_name
        self.last_name = last_name
        self.prog_lang = prog_lang


    def roll_call(self):
        print("I am a Devops Student and {} ".format(self.prog_lang))

    
student_two = Devops_student("bari","allali","python")
student_two.full_name()
student_two.roll_call()