import json

class Student:
    def __init__(self, mssv, name, major, gpa):
        self.mssv = mssv
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"MSSV: {self.mssv} | Tên: {self.name} | Ngành: {self.major} | GPA: {self.gpa}"

class StudentManager:
    def __init__(self):
        self.students = []  # List chứa các Student

    def add(self, student):
        # Kiểm tra trùng MSSV
        for s in self.students:
            if s.mssv == student.mssv:
                print(f"MSSV {student.mssv} đã tồn tại!")
                return
        self.students.append(student)
        print("Đã thêm!")

    def find_by_mssv(self, mssv):
        for s in self.students:
            if s.mssv == mssv:
                return s
        return None
    
    def delete(self, mssv):
        s = self.find_by_mssv(mssv)
        if not s:
            print("Không tìm thấy!")
            return
        self.students.remove(s)
        print("Đã xóa!")

    def show_all(self):
        if not self.students:
            print("Danh sách trống!")
            return
        for s in sorted(self.students, key = lambda x: x.gpa, reverse = True):
            print(s)
    def save(self, filename = "data.json"):
        data = []
        for s in self.students:
            data.append({
                "mssv": s.mssv,
                "name": s.name,
                "major": s.major,
                "gpa": s.gpa
            })
        with open(filename, "w", encoding = "utf-8") as f:
            json.dump(data, f, indent = 4, ensure_ascii = False)
        print(f"Đã lưu vào {filename}!")

    def load(self, filename = "data.json"):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                data = json.load(f)
            for d in data:
                self.students.append(Student(d["mssv"], d["name"], d["major"], d["gpa"]))
            print(f"Đã tải {len(self.students)} sinh viên!")
        except FileNotFoundError:
            print("Chưa có file data, bắt đầu mới!")

def menu():
    mgr = StudentManager()
    mgr.load()

    while True:
        print("\n╔══════════════════════════════╗")
        print("║  STUDENT MANAGEMENT PYTHON   ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Thêm sinh viên            ║")
        print("║ 2. Tìm theo MSSV             ║")
        print("║ 3. Xóa sinh viên             ║")
        print("║ 4. Danh sách (sort GPA)      ║")
        print("║ 0. Thoát                     ║")
        print("╚══════════════════════════════╝")

        choice = input("Lựa chọn: ")

        if choice == "1":
            mssv  = input("MSSV : ")
            name  = input("Tên  : ")
            major = input("Ngành: ")
            gpa   = float(input("GPA  : "))
            mgr.add(Student(mssv, name, major, gpa))
        elif choice == "2":
            mssv = input("Nhập MSSV: ")
            s = mgr.find_by_mssv(mssv)
            if s: print(s)
            else: print("Không tìm thấy!")
        elif choice == "3":
            mssv = input("Nhập MSSV cần xóa: ")
            mgr.delete(mssv)
        elif choice == "4":
            mgr.show_all()
        elif choice == "0":
            mgr.save()
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

menu()