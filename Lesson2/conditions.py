# ======= CÂU ĐIỀU KIỆN ========

# Dạng thiếu
age = 2
if age < 18:
    print('Bạn chưa đủ tuổi lái xe!')

# Dạng đủ
number = 10
if number % 2 == 0:
    print(number, 'là số chẵn')
else:
    print(number, 'là số lẻ')

# Dạng đa nhánh:
    # Xếp loại học lực:
    # [8, 10]: Giỏi
    # [6.5, 8): Khá
    # [5, 6.5): Trung bình
    # [0, 5): Yếu
score = 9
if 8 <= score <= 10:
    print('Học lực: Giỏi')
elif 6.5 <= score < 8:
    print('Học lực: Khá')
elif 5 <= score < 6.5:
    print('Học lực: Trung bình')
elif 0 <= score < 5:
    print('Học lực: Yếu')
else:
    print('Điểm không hợp lệ!')

# try - except: xử lý ngoại lệ
a = 10
b = 'Duy Anh'

try:
    print(a + b)
except:
    print("câu lệnh trên bị lỗi")

print('Duy Anh đẹp trai')