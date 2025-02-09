# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, can_teach_subjects: set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    assigned_teachers = []

    teacher_objects = [Teacher(*teacher) for teacher in teachers]

    while remaining_subjects:
        best_candidate = None
        max_coverage = 0

        for teacher in teacher_objects:
            possible_subjects = teacher.can_teach_subjects & remaining_subjects
            if len(possible_subjects) > max_coverage or (
                    len(possible_subjects) == max_coverage and teacher.age < (
            best_candidate.age if best_candidate else float('inf'))
            ):
                best_candidate = teacher
                max_coverage = len(possible_subjects)

        if not best_candidate:
            return None

        best_candidate.assigned_subjects = best_candidate.can_teach_subjects & remaining_subjects
        remaining_subjects -= best_candidate.assigned_subjects
        assigned_teachers.append(best_candidate)

    return assigned_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        ('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        ('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        ('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        ('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        ('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        ('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
