'''
n = int(input("Nhập chiều cao n: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
'''
n = int(input("Nhập chiều cao n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")  # khoảng trắng trước
    print("* " * i)
'''