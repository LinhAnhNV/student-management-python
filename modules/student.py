import json

class Student:
    def __init__(self, mssv, name, major, gpa):
        self.mssv  = mssv
        self.name  = name
        self.major = major
        self.gpa   = gpa
    
    def __str__(self):
        return f"MSSV: {self.mssv} | Tên: {self.name} | Ngành: {self.major} | GPA: {self.gpa}"


class StudentManager:
    def __init__(self):
        self.students = []
    
    def add(self, student):
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
        for s in sorted(self.students, key=lambda x: x.gpa, reverse=True):
            print(s)
    
    def save(self, filename="data/students.json"):
        data = []
        for s in self.students:
            data.append({
                "mssv":  s.mssv,
                "name":  s.name,
                "major": s.major,
                "gpa":   s.gpa
            })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Đã lưu vào {filename}!")
    
    def load(self, filename="data/students.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            for d in data:
                self.students.append(Student(d["mssv"], d["name"], d["major"], d["gpa"]))
            print(f"Đã tải {len(self.students)} sinh viên!")
        except FileNotFoundError:
            print("Chưa có file data, bắt đầu mới!")