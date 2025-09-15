def ngay_ke_sau(ngay, thang, nam):
    # Số ngày từng tháng (tháng 2 để 28 mặc định)
    ngay_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Kiểm tra năm nhuận
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        ngay_thang[1] = 29

    ngay += 1  # tăng ngày lên 1

    # Nếu vượt quá số ngày trong tháng thì sang tháng mới
    if ngay > ngay_thang[thang - 1]:
        ngay = 1
        thang += 1

        # Nếu vượt quá tháng 12 thì sang năm mới
        if thang > 12:
            thang = 1
            nam += 1

    return ngay, thang, nam

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tính ngày kế tiếp
ngay_moi, thang_moi, nam_moi = ngay_ke_sau(ngay, thang, nam)

print(f"Ngày kế sau: {ngay_moi}/{thang_moi}/{nam_moi}")
