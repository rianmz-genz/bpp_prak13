# app.py
import tkinter as tk
from tkinter import ttk
import easygui
from student_manager import StudentManager


class StudentManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Pengelola Mahasiswa")

        self.label = tk.Label(master, text="Daftar Mahasiswa:")
        self.label.pack()

        self.student_tree = ttk.Treeview(master, columns=("No", "Name", "NIM"), show="headings")
        self.student_tree.heading("No", text="No")
        self.student_tree.heading("Name", text="Nama")
        self.student_tree.heading("NIM", text="NIM")
        self.student_tree.pack()

        self.add_button = tk.Button(master, text="Tambah Mahasiswa", command=self.add_student)
        self.add_button.pack()

        self.edit_button = tk.Button(master, text="Edit Mahasiswa", command=self.edit_student)
        self.edit_button.pack()

        self.delete_button = tk.Button(master, text="Hapus Mahasiswa", command=self.delete_student)
        self.delete_button.pack()

        self.student_manager = StudentManager()
        self.load_students()

    def add_student(self):
        name = easygui.enterbox("Masukkan nama mahasiswa:")
        nim = easygui.enterbox("Masukkan NIM mahasiswa:")

        if name and nim:
            self.student_manager.add_student(name, nim)
            self.load_students()

    def edit_student(self):
        selected_item = self.student_tree.selection()

        if selected_item:
            student_id = self.student_tree.item(selected_item, 'values')[0]
            new_name = easygui.enterbox("Masukkan nama baru:")
            new_nim = easygui.enterbox("Masukkan NIM baru:")

            if new_name and new_nim:
                self.student_manager.edit_student(student_id, new_name, new_nim)
                self.load_students()

    def delete_student(self):
        selected_item = self.student_tree.selection()

        if selected_item:
            student_id = self.student_tree.item(selected_item, 'values')[0]
            self.student_manager.delete_student(student_id)
            self.load_students()

    def load_students(self):
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        students = self.student_manager.get_students()
        for student in students:
            self.student_tree.insert("", tk.END, values=(student[0], student[1], student[2]))


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()
