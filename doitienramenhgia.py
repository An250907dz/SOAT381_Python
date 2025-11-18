print("=== ĐỔI TIỀN RA MỆNH GIÁ ===")
so_tien = int(input("Nhập số tiền: "))
menh_gia = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]
print("Các mệnh giá cần thiết:")
for mg in menh_gia:
    so_to = so_tien // mg
    if so_to > 0:
        print(f"{mg:>6} VNĐ: {so_to} tờ")
        so_tien %= mg