from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school = School('ABC', "Dhaka")

#adding classroom
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#adding student

Mahim = Student("Mahim", eight)
Ayesha = Student("Ayesha", nine)
Nasim = Student("Nasim", ten)
Muhit = Student("Muhit", ten)

school.student_admission(Mahim)
school.student_admission(Ayesha)
school.student_admission(Nasim)
school.student_admission(Muhit)


#adding teachers

rana = Teacher("Masud Rana")
maruf = Teacher("Maruf Hasan")
azad = Teacher("Abul Kalam Azad")

#adding subbjects

bangla = Subject('Bangla', rana)
physics = Subject('Physics', azad)
chemistry = Subject('Chemistry', maruf)
biology = Subject('Biology', rana)

school.add_teacher('Bangla', rana)
school.add_teacher('Physics', azad)
school.add_teacher('Chemistry', maruf)
school.add_teacher('Biology', rana)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(biology)
ten.add_subject(bangla)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)