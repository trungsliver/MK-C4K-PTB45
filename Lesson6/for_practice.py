# Dạng 1: In / Hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = 10
for i in range(n+1):
    print(i, end=' ')
print('\n')

    # 1.2. In ra màn hình các số nguyên trong khoảng [a, b]
a, b = 5, 15
print(f'\nCác số nguyên trong khoảng [{a}, {b}] là: ')
for i in range(a, b+1):
    print(i, end=' ')

    # 1.3. In ra màn hình các số chẵn trong khoảng [a, b]
a, b = 1, 10
print(f'\nCác số chẵn trong khoảng [{a}, {b}] là: ')
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')

    # 1.4. In ra màn hình các số lẻ trong khoảng [a, b]
a, b = 1, 20
print(f'\nCác số lẻ trong khoảng [{a}, {b}] là: ')
for i in range(a, b+1):
    if i % 2 != 0:
        print(i, end=' ')

# Dạng 2: Tính tổng
    # 2.1: Tính tổng các số trong khoảng [a, b]
total = 0
a, b = 1, 5
for i in range(a, b+1):
    total = total + i   # total += i
print(f'\nTổng các số trong khoảng [{a}, {b}] là: {total}')

    # 2.2. Tính tổng các số chẵn trong khoảng [a, b]
total_even = 0
a, b = 1, 5
for i in range(a, b+1):
    if i % 2 == 0:
        total_even += i
print(f'Tổng các số chẵn trong khoảng [{a}, {b}] là: {total_even}')

# Dạng 3: Dạng đếm
    # 3.1. Đếm số lượng các số trong khoảng [a, b]
count = 0
a, b = 22, 67
for i in range(a, b+1):
    count += 1
print(f'Số lượng các số trong khoảng [{a}, {b}] là: {count}')

    # 3.2. Đếm số lượng số lẻ trong khoảng [a, b]
count_odd = 0
a, b = 22, 67
for i in range(a, b+1):
    if i % 2 != 0:
        count_odd += 1
print(f'Số lượng số lẻ trong khoảng [{a}, {b}] là: {count_odd}')