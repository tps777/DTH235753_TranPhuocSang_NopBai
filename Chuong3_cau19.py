import math
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
kq = x ** (2 * n + 1) / math.factorial(2 * n + 1)
print("Kết quả:", kq)