import pandas as pd

def xep_loai(avg):
    if avg >= 8.5: return "Xuất sắc"
    elif avg >= 7.0: return "Giỏi"
    elif avg >= 5.5: return "Khá"
    elif avg >= 4.0: return "Trung bình"
    else: return "Yếu"

def phan_tich(filename="data/grades.csv"):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("Chưa có file grades.csv trong thư mục data!")
        return

    subjects = ["math", "physics", "english", "programming"]
    df["average"] = df[subjects].mean(axis=1).round(2)
    df["rank"] = df["average"].apply(xep_loai)

    print("\n=== THỐNG KÊ TỔNG QUAN ===")
    print(df[subjects].describe().round(2))

    print("\n=== TOP 5 SINH VIÊN GIỎI NHẤT ===")
    top5 = df.nlargest(5, "average")[["mssv", "name", "average", "rank"]]
    print(top5.to_string(index=False))

    print("\n=== PHÂN PHỐI XẾP LOẠI ===")
    print(df["rank"].value_counts())

    print("\n=== TRUNG BÌNH THEO NGÀNH ===")
    print(df.groupby("major")["average"].mean().round(2))

    df.to_csv("data/report.csv", index=False, encoding="utf-8-sig")
    print("\nĐã xuất báo cáo ra data/report.csv!")