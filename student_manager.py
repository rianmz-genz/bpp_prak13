# student_manager.py
import sqlite3


class StudentManager:
    def __init__(self, db_path="students.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, nim TEXT)")
        self.connection.commit()

    def add_student(self, student_name, student_nim):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO students (name, nim) VALUES (?, ?)", (student_name, student_nim))
        self.connection.commit()

    def get_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    def edit_student(self, student_id, new_name, new_nim):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE students SET name=?, nim=? WHERE id=?", (new_name, new_nim, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.connection.commit()

    def __del__(self):
        # Close the database connection when the object is deleted
        self.connection.close()
