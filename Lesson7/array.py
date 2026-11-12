# Danh sách: Array / List
# Khái niệm: là 1 cấu trúc dữ liệu (lưu nhiều giá trị vào trong 1 biến
# Thao tác cơ bản: CRUD (Create, Read, Update, Delete

# Create: Khởi tạo danh sách
    # Danh sách rỗng (Không có phần tử)
arr = []
    # Danh sách có sẵn phần tử
ptb45 =['Duy Anh', 'Duc Trung', 'Xuân Khánh', 'Tuấn Việt', 'James']
arr1 = ['Duy Anh', 10, 8.5, True, [1,2,3,4,5]]

# Read: Duyệt, hiện phần tử
    # len(): độ dài / số lượng phần tử danh sách
print('Số lượng phần tử của arr:', len(arr))
print('Số lượng phần tử của ptb45:', len(ptb45))
print('Số lượng phần tử của arr1:', len(arr1))

    # Hiển thị phần tử theo index
print('Phần tử đầu tiên:', ptb45[0])
print('Phần tử thứ 2:', ptb45[2])
print('Phần tử cuối cùng:', ptb45[len(ptb45)-1])
print('Phần tử cuối cùng:', ptb45[-1])

    # Hiển thị toàn bộ danh sách
print('Danh sách ptb45:', ptb45)

    # Duyệt danh sách
        # Cách 1: Dùng cả index và value
for i in range(len(ptb45)):
    print(f'Index: {i}. Value: {ptb45[i]}')
        # Cách 2: Chỉ dung value
for item in ptb45:
    print('Value:', item)
        # Cách 3: Dùng hàm có sẵn 
for index, value in enumerate(ptb45):
    print(f'Index: {index}. Value: {value}')

# Update - Cập nhật phần tử
    # Thêm vào cuối danh sách - append(value)
ptb45.append('Donald Trump')
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
ptb45.insert(2, 'imposter')
    # Sửa phần tử cũ
ptb45[2] = 'Putin'

# Delete - Xóa phần tử
    # Xóa theo index - pop(index)
ptb45.pop(2)
    # Xóa theo value - remove(value)
ptb45.remove('Donald Trump')
    # Xóa tất cả phần tử - clear()
ptb45.clear()

# Sắp xếp phần tử
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự tăng dần - sort()
num_list.sort()
print('Danh sách tăng dần:', num_list)
    # Theo thứ tự giảm dần - sort(reverse=True)
num_list.sort(reverse=True)
print('Danh sách giảm dần:', num_list)

# Giá trị lớn nhất, nhỏ nhất
print('Giá trị lớn nhất:', max(num_list))
print('Giá trị nhỏ nhất:', min(num_list))