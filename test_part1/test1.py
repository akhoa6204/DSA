s = input()
for i in s: 
   print("0" + bin(ord(i))[2:], end=" ") 
# ord: chữ sang số trong bảng mã ascii 
# chr: chuyển số sang chữ trong bảng mã ascii
# bin chuyển sang hệ nhị phân !!! mỗi chữ khi chuyển đổi sẽ có 0b ở đầu
# 1B