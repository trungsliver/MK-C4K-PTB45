# =============== LUYỆN TẬP ===============
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
for i in range(a, b + 1):
    print(i)

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b
a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
if b >= a:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(b, a + 1):
        print(i)

# Bài 3: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a
a = int(input('Nhập số nguyên a trong khoảng [1, 10]: '))
print(f'Bảng cửu chương {a}:')
for i in range(1, 11):
    print(f'{a} x {i} = {a * i}')

# Bài 4: In ra màn hình bảng cửu chương từ 2 => 9
for a in range(2, 10):
    print(f'\nBảng cửu chương {a}:')
    for i in range(1, 11):
        print(f'{a} x {i} = {a * i}')

# Bài 5: Nhập số nguyên n trong khoảng [0, 100]
# Nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
n = int(input('Nhập số nguyên n trong khoảng [0, 100]: '))
while n < 0 or n > 100:
    print('Nhập sai. Vui lòng nhập lại.')
    n = int(input('Nhập số nguyên n trong khoảng [0, 100]: '))
print(f'Bạn đã nhập đúng: {n}')

# Bài 6: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Khi người chơi đoán đúng, hiển thị số lần người chơi đã đoán
