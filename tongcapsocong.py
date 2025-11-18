print("=== TỔNG CẤP SỐ CỘNG ===")
u1 = float(input("Nhập số hạng đầu u1: "))
d = float(input("Nhập công sai d: "))
n = int(input("Nhập số phần tử n: "))
tong = n * (2 * u1 + (n - 1) * d) / 2
print(f"Tổng {n} số hạng đầu: {tong:.2f}")