print("=== CHUYỂN ĐỔI THẬP PHÂN SANG NHỊ PHÂN ===")
so = int(input("Nhập số nguyên thập phân: "))
nhi_phan = bin(so)[2:]  # bỏ tiền tố '0b'
print(f"Số nhị phân: {nhi_phan}")