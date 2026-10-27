class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)


    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <=100:
            return 'A+'
        elif marks >= 70 and marks <80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks <50:
            return 'C'
        elif marks >= 33 and marks <40:
            return 'D'
        else: 
            return 'F'


    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-': 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]


    @staticmethod
    def value_to_grade(value):
        if value >= 5.00:
            return 'A+'
        elif value >= 4.0 and value < 5.00:
            return 'A'
        elif value >= 3.5 and value < 4.0:
            return 'A-'
        elif value >= 3.0 and value < 3.5:
            return 'B'
        elif value >= 2.0 and value < 3.0:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else :
            return 'F'


    def __repr__(self):
        width = 50
        line = "=" * width
        divider = "-" * width

        # Header
        result = f"{line}\n"
        result += f"{'SCHOOL MANAGEMENT REPORT':^{width}}\n"
        result += f"{f'{self.name}, {self.address}':^{width}}\n"
        result += f"{line}\n"

        # All Classrooms
        result += f"\nCLASSROOMS\n{divider}\n"
        result += f"{'Class':<12}{'Students':>10}{'Subjects':>10}\n"
        for key, value in self.classrooms.items():
            result += f"{key:<12}{len(value.students):>10}{len(value.subjects):>10}\n"

        # All Students
        result += f"\nSTUDENTS\n{divider}\n"
        result += f"{'ID':<12}{'Name':<18}{'Class':<10}\n"
        for key, value in self.classrooms.items():
            for student in value.students:
                result += f"{student.id:<12}{student.name:<18}{key:<10}\n"

        # All Subjects
        result += f"\nSUBJECTS\n{divider}\n"
        result += f"{'Class':<12}{'Subject':<14}{'Teacher':<18}\n"
        for key, value in self.classrooms.items():
            for sub in value.subjects:
                result += f"{key:<12}{sub.name:<14}{sub.teacher.name:<18}\n"

        # All Teachers
        result += f"\nTEACHERS\n{divider}\n"
        result += f"{'Teacher':<20}{'Subjects'}\n"
        teacher_subjects = {}
        for subject, teacher in self.teachers.items():
            teacher_subjects.setdefault(teacher.name, []).append(subject)
        for name, subjects in teacher_subjects.items():
            result += f"{name:<20}{', '.join(subjects)}\n"

        # All Student Results
        result += f"\n{line}\n{'STUDENT RESULTS':^{width}}\n{line}\n"
        for key, value in self.classrooms.items():
            for student in value.students:
                result += f"\n{student.name} ({student.id})\n"
                result += f"  {'Subject':<14}{'Marks':>6}   {'Grade'}\n"
                for k, i in student.marks.items():
                    result += f"  {k:<14}{i:>6}   {student.subject_grade[k]}\n"
                result += f"  {'-' * 28}\n"
                result += f"  {'GPA':<14}{student.gpa:>6.2f}   {student.grade}\n"
        result += f"\n{line}"
        return result