print("=== CHUYỂN ĐỔI GIÂY SANG GIỜ:PHÚT:GIÂY ===")
tong_giay = int(input("Nhập số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"Thời gian: {gio:02d}:{phut:02d}:{giay:02d}")