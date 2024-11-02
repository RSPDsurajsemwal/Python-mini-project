import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance System")
        self.root.geometry("1000x800")
        self.root.config(bg="#f0f0f0")

        # Create background frames for mixed color effect
        self.bg_frame1 = tk.Frame(self.root, bg="#F8F8FF")
        self.bg_frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.bg_frame2 = tk.Frame(self.root, bg="#F8F8FF")
        self.bg_frame2.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        # Title Label
        self.title_label = tk.Label(self.root, text="Student Attendance System", font=('Arial', 15), bg="blue", fg="#fff")
        self.title_label.pack(fill='x', pady=8)

        # Load images using Pillow
        self.left_image = Image.open("C:/Users/MADHAV/Desktop/python projext/New folder/stud.jpg")
        self.left_image = self.left_image.resize((500, 200))
        self.left_image = ImageTk.PhotoImage(self.left_image)

        self.right_image = Image.open("C:/Users/MADHAV/Desktop/python projext/New folder/board.jpg")
        self.right_image = self.right_image.resize((500, 200))
        self.right_image = ImageTk.PhotoImage(self.right_image)

        self.centre_image = Image.open("C:/Users/MADHAV/Desktop/python projext/New folder/professor.jpg")
        self.centre_image = self.centre_image.resize((450, 200))
        self.centre_image = ImageTk.PhotoImage(self.centre_image)

        # Display images
        self.left_image_label = tk.Label(self.root, image=self.left_image, bg="#f0f0f0")
        self.left_image_label.place(relx=0.00, rely=0.05, anchor='nw')

        self.right_image_label = tk.Label(self.root, image=self.right_image, bg="#f0f0f0")
        self.right_image_label.place(relx=1.0, rely=0.05, anchor='ne')

        self.centre_image_label = tk.Label(self.root, image=self.centre_image, bg="#f0f0f0")
        self.centre_image_label.place(relx=0.50, rely=0.05, anchor='n')

        # In-memory database
        self.students = []

        # Search Frame
        self.search_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.search_frame.place(relx=0.3, rely=0.34, anchor='nw')

        tk.Label(self.search_frame, text="Student Name:", font=('Arial', 14), bg="#f0f0f0").pack(side='left', padx=5)
        self.search_entry = tk.Entry(self.search_frame, font=('Arial', 12), width=25)
        self.search_entry.pack(side='left', padx=5)
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_student, font=('Arial', 12), bg="#4CAF50", fg="white")
        self.search_button.pack(side='left', padx=5)

        # Personal Details Frame
        self.personal_frame = tk.LabelFrame(self.root, text="Personal Details", bg="#e0e0e0", font=('Arial', 14))
        self.personal_frame.place(relx=0.0, rely=0.39, anchor='nw', width=500, height=250)

        labels = ["First Name:", "Last Name:", "Phone No:", "UID No:", "Father's Name:", "Address:"]
        self.personal_entries = []
        for i, label in enumerate(labels):
            tk.Label(self.personal_frame, text=label, bg="#e0e0e0", font=('Arial', 12)).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(self.personal_frame, font=('Arial', 12))
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.personal_entries.append(entry)

        self.first_name_entry, self.last_name_entry, self.phone_entry, self.uid_entry, self.father_name_entry, self.address_entry = self.personal_entries

        # Course Details Frame
        self.course_frame = tk.LabelFrame(self.root, text="Course Details", bg="#e0e0e0", font=('Arial', 14))
        self.course_frame.place(relx=0.3, rely=0.39, anchor='nw', width=550, height=250)

        tk.Label(self.course_frame, text="Course Name:", bg="#e0e0e0", font=('Arial', 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.course_name_entry = ttk.Combobox(self.course_frame, values=[
            "MCA",
            "MCA in AI/ML",
            "MCA in Cloud Computing"
        ], state="readonly", font=('Arial', 12))
        self.course_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.course_frame, text="Section:", bg="#e0e0e0", font=('Arial', 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.section_entry = ttk.Combobox(self.course_frame, values=["A", "B", "C"], state="readonly", font=('Arial', 12))
        self.section_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.course_frame, text="Group:", bg="#e0e0e0", font=('Arial', 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.group_entry = ttk.Combobox(self.course_frame, values=[1, 2, 3, 4, 5], state="readonly", font=('Arial', 12))
        self.group_entry.grid(row=2, column=1, padx=5, pady=5)

        # Teacher's Details Frame
        self.teacher_frame = tk.LabelFrame(self.root, text="Teacher's Details", bg="#e0e0e0", font=('Arial', 14))
        self.teacher_frame.place(relx=0.7, rely=0.39, anchor='nw', width=520, height=250)

        teacher_labels = ["Teacher Name:", "Class Time:", "Room No:", "Date:"]
        self.teacher_entries = []
        self.teacher_names = [
            "Mrs. Deepali Saini", "Mr. Rishabh Tomar", "Mr. Paras Sen", 
            "Mrs. Prabhjyot Kaur", "Ms. Muskan", "Mr. Abdullah"
        ]
        for i, label in enumerate(teacher_labels):
            tk.Label(self.teacher_frame, text=label, bg="#e0e0e0", font=('Arial', 12)).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            if label == "Teacher Name:":
                entry = ttk.Combobox(self.teacher_frame, values=self.teacher_names, state="readonly", font=('Arial', 12))
            elif label == "Class Time:":
                entry = ttk.Combobox(self.teacher_frame, values=[f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in (0, 30)], state="readonly", font=('Arial', 12))
            elif label == "Date:":
                entry = DateEntry(self.teacher_frame, font=('Arial', 12), width=12)
            else:
                entry = tk.Entry(self.teacher_frame, font=('Arial', 12))
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.teacher_entries.append(entry)

        self.teacher_name_entry, self.class_time_entry, self.room_no_entry, self.date_entry = self.teacher_entries

        # Attendance Record Frame
        self.record_frame = tk.LabelFrame(self.root, text="Attendance Record", bg="#e0e0e0", font=('Arial', 14))
        self.record_frame.place(relx=0.0, rely=0.74, anchor='nw', width=990, height=138)

        # Create a frame for the Treeview and Scrollbar
        self.tree_frame = tk.Frame(self.record_frame)
        self.tree_frame.pack(fill='both', expand=True)

        self.attendance_tree = ttk.Treeview(self.tree_frame, columns=("UID", "Name", "Course", "Room No", "Group", "Attendance"), show='headings', height=6)
        self.attendance_tree.pack(side='left', fill='both', expand=True)

        # Create a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient='vertical', command=self.attendance_tree.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Configure the Treeview to use the scrollbar
        self.attendance_tree.configure(yscrollcommand=self.scrollbar.set)

        for col in self.attendance_tree["columns"]:
            self.attendance_tree.heading(col, text=col)
            self.attendance_tree.column(col, width=80)

        # Button Frame for Attendance Actions
        self.button_frame = tk.Frame(self.root, bg="#e0e0e0")
        self.button_frame.place(relx=0.9, rely=0.75, anchor='ne')

        self.add_button = tk.Button(self.button_frame, text="Add Student", command=self.add_student, font=('Arial', 12), bg="#2196F3", fg="white")
        self.add_button.pack(pady=5)

        self.mark_attendance_button = tk.Button(self.button_frame, text="Mark Attendance", command=self.mark_attendance, font=('Arial', 12), bg="#FF9800", fg="white")
        self.mark_attendance_button.pack(pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Student", command=self.delete_student, font=('Arial', 12), bg="#F44336", fg="white")
        self.delete_button.pack(pady=5)

    def load_students(self):
        self.attendance_tree.delete(*self.attendance_tree.get_children())  # Clear the tree view before loading
        for student in self.students:
            self.attendance_tree.insert("", "end", values=(student['uid'], f"{student['first_name']} {student['last_name']}", student['course'], student['room_no'], student['group_no'], student['attendance']))

    def add_student(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        uid = self.uid_entry.get().strip()
        father_name = self.father_name_entry.get().strip()
        address = self.address_entry.get().strip()
        course = self.course_name_entry.get().strip()
        section = self.section_entry.get()
        group_no = self.group_entry.get()
        teacher_name = self.teacher_name_entry.get()
        class_time = self.class_time_entry.get()
        room_no = self.room_no_entry.get()
        date = self.date_entry.get()

        # Validate inputs
        if not all([first_name, last_name, phone, uid, father_name, address, course, section, group_no, teacher_name, class_time, room_no, date]):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        if len(phone) != 10 or not phone.isdigit():
            messagebox.showwarning("Input Error", "Phone number must be 10 digits.")
            return

        # Add student to the in-memory database
        student = {
            'uid': uid,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'father_name': father_name,
            'address': address,
            'course': course,
            'section': section,
            'group_no': int(group_no),
            'teacher_name': teacher_name,
            'class_time': class_time,
            'room_no': room_no,
            'date': date,
            'attendance': False
        }
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully.")
        self.load_students()

    def mark_attendance(self):
        selected_item = self.attendance_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to mark attendance.")
            return

        uid = self.attendance_tree.item(selected_item)['values'][0]
        for student in self.students:
            if student['uid'] == uid:
                student['attendance'] = True
                break
        messagebox.showinfo("Success", "Attendance marked as present.")
        self.load_students()

    def delete_student(self):
        selected_item = self.attendance_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return

        uid = self.attendance_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the student with UID: {uid}?")
        if confirm:
            self.students = [student for student in self.students if student['uid'] != uid]
            messagebox.showinfo("Success", "Student deleted successfully.")
            self.load_students()

    def search_student(self):
        name = self.search_entry.get().strip()
        filtered_students = [student for student in self.students if name.lower() in student['first_name'].lower() or name.lower() in student['last_name'].lower()]

        self.attendance_tree.delete(*self.attendance_tree.get_children())  # Clear previous results
        for student in filtered_students:
            self.attendance_tree.insert("", "end", values=(student['uid'], f"{student['first_name']} {student['last_name']}", student['course'], student['room_no'], student['group_no'], student['attendance']))

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSystem(root)
    root.mainloop()
