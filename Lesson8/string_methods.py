# ========== Các hàm thường dùng với string ==========

# String - chuỗi / xâu ký tự
class_name = "Python App Basic 45"
name = 'Duy Anh'

# Độ dài string (số ký tự) - len()
print('Độ dài class_name:', len(class_name))
print('Độ dài name:', len(name))

# Truy cập ký tự trong string 
    # Truy cập theo index
print('Ký tự đầu tiên:', name[0])
print('Ký tự cuối cùng:', name[len(name)-1])
print('Ký tự cuối cùng (cách 2):', class_name[-1])

    # Duyệt string
        # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'Index {i} - Value: {name[i]}')

        # Cách 2: Dùng value
for char in name:
    print('Value:', char)

# Xâu con (sub string)
str1 = 'Do Duy Anh'
str2 = 'Duy Anh'
str3 = 'dep trai'

    # kiểm tra substring: in
print('str2 in str1:', str2 in str1)
print('str3 in str1:', str3 in str1)

    # Tìm vị trí sub string: find()
print('Vị trí str2 trong str1:', str1.find(str2))   # 3
print('Vị trí str3 trong str1:', str1.find(str3))   # -1 (không tìm thấy)

# Cắt chuỗi - slicing()
name = 'hahahihihuhu'
    # cắt ở vị trí bất kì [start:stop]
print('Cắt từ index 4 -> 8:', name[4:8])   # hihi
    # cắt từ đầu string [:stop]
print('Cắt từ đầu -> index 4:', name[:4])   # haha
    # cắt đến cuối string [start:]
print('Cắt từ index 8 -> cuối:', name[8:])   # huhu

# Tách string => trả về danh sách - split()
    # mặc định: tách khi gặp khoảng trắng
str1 ='1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('arr1:', arr1)

    # Tách khi gặp ký tự bất kì
str2 = 'a,b,c,d,e,f,g,h'
arr2 = str2.split(',')
print('arr2:', arr2)

# Xóa khoảng trắng ở đầu và cuối - strip()
name = '         Duy Anh             '
print('Trước strip():', name)
print('Sau strip():', name.strip())

# Thay thế string - replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ: replace(old, new)
song2 = song.replace('doo', 'nam')
print('song2 =', song2) 
    # Thay thế 1 phần: replace(old, new, count)
song3 = song.replace('doo', 'nam', 3)
print('song3 =', song3)

# Kết hợp chuỗi - join()
arr = ['r', 'o', 'n', 'a', 'l', 'd', 'o']
    # Kết hợp với khoảng trắng
str1 = ' '.join(arr)
print('str1 =', str1)
    # Kết hợp với ký tự bất kì
str2 = ''.join(arr)
print('str2 =', str2)

str3 = '-'.join(arr)
print('str3 =', str3)

# Chuẩn hóa string
name = 'dO dUy aNH'
    # Viết hoa tất cả: upper()
print('Viết hoa:', name.upper())
    # Viết thường tất cả: lower()
print('Viết thường:', name.lower())
    # Viết hoa chữ cái đầu: title()
print('Viết hoa chữ cái đầu:', name.title())

# ========= Ví dụ ==========
# Bài 1: Chuyển đổi kiểu dữ liệu của tất cả phần tử danh sách
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Cách 1:
arr1 = []
for item in arr: 
    new_item = int(item)
    arr1.append(new_item)
print('arr1 =', arr1)
    
    # Cách 2: Viết tắt
arr2 = [int(item) for item in arr]
print('arr2 =', arr2)

# Bài 2: Tính tổng phần tử chẵn
    # cách cũ:
total_even = 0
for item in arr2:
    if item % 2 == 0:
        total_even += item
print('Tổng phần tử chẵn =', total_even)

    # cách mới: Viết tắt
total_even2 = sum([item for item in arr2 if item % 2 == 0])
print('Tổng phần tử chẵn 2 =', total_even2)

# bài 3: đếm số phần tử chia hết cho 3
count = sum([1 for item in arr2 if item % 3 == 0])
print('Số phần tử chia hết cho 3 =', count)