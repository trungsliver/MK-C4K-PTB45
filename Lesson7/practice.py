# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

n = int(input('Nhập số nguyên n: '))
    # Biến count đếm số lượng ước của n
count = 0

    # Duyệt i trong khoảng từ 1 đến n
for i in range(1, n+1):
    # Nếu n chia hết cho i thì tăng biến count lên 1
    if n % i == 0:
        count += 1

    # Hiển thị kết quả
if count == 2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
total = 0

    # Duyệt n trong khoảng [50,100]
for n in range(50, 101):
    # Biến count đếm số lượng ước của n
    count = 0
    # Duyệt i trong khoảng từ 1 đến n
    for i in range(1, n+1):
        # Nếu n chia hết cho i thì tăng biến count lên 1
        if n % i == 0:
            count += 1
    # Hiển thị kết quả
    if count == 2:
        print(n, end=' ')
        total += n
        
print(f'\nTổng các số nguyên tố trong khoảng [50,100] là: {total}')    