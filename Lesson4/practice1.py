# Bài 1: Chuyển đổi USD sang VND
    # Nhập số USD muốn chuyển (float)
usd = float(input("Nhập số USD muốn chuyển: $"))
    # Đổi usd sang vnd
vnd = usd * 26000   
    # Hiển thị kết quả
print(f"{usd}$ = {vnd} VND")

# Bài 2: Nhập chiều dài, chiều rộng của HCN
# Tính diện tích và chu vi của HCN
length = float(input('Nhập chiều dài của HCN: '))
width = float(input('Nhập chiều rộng của HCN: '))
    # Tính diện tích và chu vi
area = length * width
perimeter = 2 * (length + width)
    # Hiển thị kết quả
print('Diện tích của HCN là:', area)
print('Chu vi của HCN là:', perimeter)

# Bài 3: Viết chương trình nhập vào 1 số nguyên
# Kiểm tra số đó là chẵn hay lẻ.
number = int(input('Nhập 1 số nguyên: '))
if number % 2 == 0:
    print(number, "là số chẵn")
else:
    print(number, "là số lẻ")

# Bài 4: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND / kWh
# Bậc 2:    51kWh - 100kWh         giá 2k VND / kWh
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND / kWh
# Bậc 4:    trên 201kWh            giá 3k VND / kWh