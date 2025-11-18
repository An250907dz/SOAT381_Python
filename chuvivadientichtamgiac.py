import math

print("=== CHU VI VÀ DIỆN TÍCH TAM GIÁC ===")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
chu_vi = a + b + c
p = chu_vi / 2  # nửa chu vi
dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")