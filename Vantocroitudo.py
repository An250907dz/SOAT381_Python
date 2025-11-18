import math

print("=== VẬN TỐC RƠI TỰ DO ===")
h = float(input("Nhập độ cao h (m): "))
g = 9.8  # gia tốc trọng trường
v = math.sqrt(2 * g * h)
print(f"Vận tốc khi chạm đất: {v:.2f} m/s")