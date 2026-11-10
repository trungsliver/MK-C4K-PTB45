# Bài 1: Nhập số nguyên n trong khoảng [0, 100]
# Nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# try:
#     n = int(input("Nhập số nguyên n trong khoảng [0, 100]: "))
#     while n < 0 or n > 100:
#         print('Bạn đã nhập sai, vui lòng nhập lại!')
#         n = int(input("\nNhập số nguyên n trong khoảng [0, 100]: "))
#     print('Bạn đã nhập đúng!')
# except:
#     print('Bạn đã nhập sai, vui lòng nhập lại!')

# Bài 2: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Khi người chơi đoán đúng, hiển thị số lần người chơi đã đoán

# Tạo số ngẫu nhiên
import random
special_number = random.randint(1, 100)
print(special_number)

try:
    guess = int(input("Nhập dự đoán của bạn: "))
    count = 1
    while guess != special_number:
        if guess > special_number:
            print('Số bạn nhập lớn hơn số đặc biệt!')
        else:
            print('Số bạn nhập nhỏ hơn số đặc biệt!')
        guess = int(input("\nNhập dự đoán của bạn: "))
        count = count + 1
    print(f'Chúc mừng bạn đã đoán đúng sau {count} lần.')
except:
    print('Bạn đã thua!')