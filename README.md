# Student Management System (Python)

Hệ thống quản lý sinh viên và phân tích điểm thi viết bằng Python — kết hợp OOP, Pandas, JSON và CSV.

Bắt đầu từ 2 project riêng lẻ, gộp lại thành 1 hệ thống hoàn chỉnh — quản lý sinh viên và phân tích điểm thi dùng chung dữ liệu.

> A unified student management and grade analysis system in Python using OOP, Pandas, JSON, and CSV.

---

## Tính năng / Features

**Quản lý sinh viên:**
- Thêm / xóa / tìm kiếm sinh viên
- Xếp hạng theo GPA
- Lưu và tải dữ liệu từ file JSON

**Phân tích điểm thi:**
- Đọc dữ liệu từ file CSV
- Tính điểm trung bình từng sinh viên
- Xếp loại tự động — Xuất sắc / Giỏi / Khá / Trung bình / Yếu
- Thống kê tổng quan theo từng môn
- Top 5 sinh viên giỏi nhất
- Thống kê trung bình theo ngành
- Xuất báo cáo ra file CSV

---

## Cấu trúc / Structure

student-management-python/
├── modules/
│   ├── student.py    # Class Student, StudentManager
│   └── analysis.py  # Phân tích điểm thi
├── data/
│   ├── students.json # Dữ liệu sinh viên
│   ├── grades.csv    # Dữ liệu điểm thi
│   └── report.csv    # Báo cáo xuất ra (tự tạo khi chạy)
├── main.py           # Menu chính
├── .gitignore
└── README.md

---

## Yêu cầu / Requirements

- Python 3.x
- Pandas
- NumPy

```bash
pip install pandas numpy
```

---

## Chạy chương trình / Run

```bash
python main.py
```

---

## Thư viện sử dụng / Libraries

| Thư viện | Dùng để |
|---|---|
| `pandas` | Đọc CSV, DataFrame, thống kê, groupby |
| `numpy` | Tính toán số học |
| `json` | Lưu và tải dữ liệu sinh viên |

---

## Tác giả / Author

**Nguyễn Văn Linh Anh**  
Sinh viên CNTT — ĐH Công Thương TP.HCM (HUIT)  
Củ Chi, TP.HCM · 2025