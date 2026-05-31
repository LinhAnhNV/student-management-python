from modules.student import Student, StudentManager
from modules.analysis import phan_tich

def menu_quan_ly(mgr):
    while True:
        print("\n╔══════════════════════════════╗")
        print("║     QUẢN LÝ SINH VIÊN        ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Thêm sinh viên            ║")
        print("║ 2. Tìm theo MSSV             ║")
        print("║ 3. Xóa sinh viên             ║")
        print("║ 4. Danh sách (sort GPA)      ║")
        print("║ 0. Quay lại                  ║")
        print("╚══════════════════════════════╝")

        choice = input("Lựa chọn: ")

        if choice == "1":
            mssv  = input("MSSV  : ")
            name  = input("Tên   : ")
            major = input("Ngành : ")
            gpa   = float(input("GPA   : "))
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
            break
        else:
            print("Lựa chọn không hợp lệ!")

def main():
    mgr = StudentManager()
    mgr.load()

    while True:
        print("\n╔══════════════════════════════════╗")
        print("║     STUDENT MANAGEMENT SYSTEM    ║")
        print("╠══════════════════════════════════╣")
        print("║ 1. Quản lý sinh viên             ║")
        print("║ 2. Phân tích điểm thi            ║")
        print("║ 0. Thoát                         ║")
        print("╚══════════════════════════════════╝")

        choice = input("Lựa chọn: ")

        if choice == "1":
            menu_quan_ly(mgr)
        elif choice == "2":
            phan_tich()
        elif choice == "0":
            mgr.save()
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

main()