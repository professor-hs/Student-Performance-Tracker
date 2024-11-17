
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = [0] * 5  # Attendance for 5 subjects
        self.marks = [0] * 5  # Marks for 5 subjects
        self.cgpa = 0.0

    def calculate_cgpa(self):
        total_marks = sum(self.marks)
        self.cgpa = total_marks / 5  # Average marks as CGPA

    def is_allowed_for_exam(self):
        # If attendance is less than 75% in any subject, not allowed for exams
        return all(att >= 75 for att in self.attendance)

class StudentPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance Tracker")

        # Create a label for the student's name
        self.name_label = tk.Label(root, text="Enter Student Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        # Create fields for marks and attendance
        self.marks_entries = []
        self.attendance_entries = []

        for i in range(5):
            # Marks Entry
            tk.Label(root, text=f"Subject {i+1} Marks:").grid(row=i+1, column=0)
            marks_entry = tk.Entry(root)
            marks_entry.grid(row=i+1, column=1)
            self.marks_entries.append(marks_entry)

            # Attendance Entry
            tk.Label(root, text=f"Subject {i+1} Attendance:").grid(row=i+1, column=2)
            attendance_entry = tk.Entry(root)
            attendance_entry.grid(row=i+1, column=3)
            self.attendance_entries.append(attendance_entry)

        # Button to calculate and show the results
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_results)
        self.calculate_button.grid(row=6, column=0, columnspan=4)

    def calculate_results(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter the student's name.")
            return
        
        # Create a student object
        student = Student(name)
        
        # Get marks and attendance from the user input
        try:
            for i in range(5):
                student.marks[i] = float(self.marks_entries[i].get())
                student.attendance[i] = float(self.attendance_entries[i].get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for marks and attendance.")
            return

        student.calculate_cgpa()
        allowed_for_exam = student.is_allowed_for_exam()

        # Display the results in a message box
        result_message = f"Student: {student.name}
"
        result_message += f"CGPA: {student.cgpa}
"
        result_message += f"Allowed for Exam: {'Yes' if allowed_for_exam else 'No'}"
        
        messagebox.showinfo("Results", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPerformanceApp(root)
    root.mainloop()