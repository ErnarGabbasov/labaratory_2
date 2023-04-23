import sqlite3

def find_databaseStudents(student_name, disciplin):
    connection = sqlite3.connect('sqlite_students.db')
    cursor = connection.cursor()
    if disciplin != 'Все дисциплины':
        cursor.execute(f'SELECT * FROM student JOIN activity ON student.ID = activity.student_id WHERE student.Name=\'{student_name}\' AND activity.Disciplines=\'{disciplin}\'') # Запрос к базе данных
    else:
        cursor.execute(f'SELECT * FROM student JOIN activity ON student.ID = activity.student_id WHERE student.Name=\'{student_name}\'')
    result = cursor.fetchall() # Получаем результат запроса
    return result