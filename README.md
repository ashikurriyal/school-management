# School Management System

A simple Python project for practising Object-Oriented Programming. It models a school with classrooms, students, teachers and subjects, runs exams and prints each student's results.

## How It Works

1. Create a `School` and add classrooms (Eight, Nine, Ten).
2. Admit students. Each one joins their classroom and gets a roll ID like `Eight-1`.
3. Create teachers and subjects, and add the subjects to classrooms.
4. Run the semester final exam. Each teacher gives a random mark (1–100), which becomes a grade (A+ to F).
5. Each student's GPA is the average of their grade points, and that GPA gives the final grade.
6. `print(school)` shows the full report.

## What I Learned

- **Classes and objects:** `School`, `Classroom`, `Subject`, `Teacher`, `Student`
- **Inheritance:** `Teacher` and `Student` extend `Person`
- **`super()`:** calling the parent's `__init__`
- **Encapsulation:** a private `__id` accessed through `@property` and a setter
- **Static methods:** grading helpers in `School` that need no instance
- **Composition:** a school holds classrooms, and classrooms hold students and subjects
- **`__repr__`:** customising what `print(school)` shows

## Files

| File | Contains |
|---|---|
| `person.py` | `Person`, `Teacher`, `Student` |
| `subject.py` | `Subject` |
| `classroom.py` | `Classroom` |
| `school.py` | `School` |
| `main.py` | Runs the program |

## Run

```bash
python3 main.py
```
