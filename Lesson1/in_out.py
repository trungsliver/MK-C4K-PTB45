# Các cách hiển thị dữ liệu
name = 'Duc Trung'
age = 2
score = 8.5

    # Cách 1: Dùng dấu cộng
print('Họ tên: ' + name)
print('Tuổi: ' + str(age))

    # Cách 2: Dùng dấu phẩy
print('Họ tên:', name)
print('Tuổi:', age)
print('Điểm:', score)

    # Cách 3: Dùng f-string
print('Tôi tên là ' + name + ', đang ' + str(age) + ' tuổi.') 
print(f'Tôi tên là {name}, đang {age} tuổi.')

    # Cách 4: Hiển thị trên nhiều dòng
print(f'''
Name: {name}
Age: {age}
Score: {score}
''')
    
# Lưu ý:
    # \n: xuống dòng
print('Dòng 1 \nDòng 2 \nDòng 3')
    # \t: tab (1 tab = 4 space)
print('Cột 1 \tCột 2 \tCột 3')
    # kết thúc print: end = 
print('1', end = ' ')
print('2', end = ' ')
print('3')

# Nhập dữ liệu - input()
    # Mặc định khi nhập, kiểu dữ liệu là string
game = input('Nhập game bạn thích: ')
print('Giá trị vừa nhập:', game)
print('Kiểu dữ liệu vừa nhập:', type(game))

    # Xác định kiểu dữ liệu khi nhập
age = int(input('Nhập tuổi của bạn: '))
print('Giá trị vừa nhập:', age)
print('Kiểu dữ liệu vừa nhập:', type(age))