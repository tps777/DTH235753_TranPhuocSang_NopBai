def doc_so(n):
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return don_vi[n]
    else:
        dv = n % 10
        ch = n // 10

        # Trường hợp đặc biệt khi số hàng chục là 1
        if ch == 1:
            if dv == 0:
                return "mười"
            elif dv == 5:
                return "mười lăm"
            else:
                return "mười " + don_vi[dv]

        # Trường hợp hàng chục > 1
        else:
            if dv == 0:
                return chuc[ch]
            elif dv == 1:
                return chuc[ch] + " mốt"
            elif dv == 4:
                return chuc[ch] + " tư"
            elif dv == 5:
                return chuc[ch] + " lăm"
            else:
                return chuc[ch] + " " + don_vi[dv]

# Nhập số từ bàn phím
n = int(input("Nhập số (0-99): "))

if 0 <= n <= 99:
    print(doc_so(n).capitalize())
else:
    print("Vui lòng nhập số từ 0 đến 99!")
    