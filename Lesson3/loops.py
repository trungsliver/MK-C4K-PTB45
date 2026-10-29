# ======== For loops ========
# Vòng lặp hữu hạn: biết trước số lần lặp

# range(start, stop, step)
    # start: giá trị bắt đầu (không bắt buộc, mặc định = 0)
    # stop: giá trị kết thúc (bắt buộc)
    # step: bước nhảy (không bắt buộc, mặc định = 1)
# Lưu ý: chạy từ start đến stop-1

# TH1: range(start, stop, step)
for i in range(1, 10, 2):
    print(i, end = ' ')  

# TH2: range(start, stop)
for i in range(1, 10):
    print(i, end = ' ')

# TH3: range(stop)
for i in range(10):
    print(i, end = ' ') 

# ======== While loops ======== 
# Vòng lặp vô hạn: không biết trước số lần lặp
# Lặp đến khi điều kiện sai
i = 1
while i <= 10:
    print(i)
    i = i + 1   # i += 1