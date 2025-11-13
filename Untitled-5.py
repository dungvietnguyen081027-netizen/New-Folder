try:
    a = int(input("nhap so nguyen a: ").strip())
    b = int(input("nhap so nguyen b: ").strip())

    tong = a + b
    hieu = a - b
    tich = a * b

    print("tong:", tong)
    print("hieu:", hieu)
    print("tich:", tich)

    if b == 0:
        print("khong the chia cho 0")
    else:
        phan_nguyen = a // b           # phép chia lấy phần nguyên
        phan_du = a % b               # phần dư
        ket_qua_chia_thuc = a / b     # chia thực (float)
        print("phan nguyen:", phan_nguyen)
        print("phan du:", phan_du)
        print("ket qua chia thuc:", ket_qua_chia_thuc)
except ValueError:
    print("vui long nhap so nguyen!")
