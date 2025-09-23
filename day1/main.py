# Ctrl + ,
print("Hello World")
print("My name is Nga")
# Vào Setting/Extension/ Run code configuration tích chọn Clear Previous Code 
# -> Để lxóa sạch những kết quả đã chạy trước đó
# Win + .: Để hiển thị bảng biểu tượng cảm xúc
# Để chạy ra biểu tượng cảm xúc cần vào Setting/Extension/ Run code configuration
# -> Excuter Map: Ở dòng Python: Sửa lại thành: set PYTHONIOENCODING=utf8 && python -u
print("❤️🤣")
# 1. Kiểu dữ liệu
# In ra loại dữ liệu:
print(type(2.0))
# Chuyển từ loại dữ liệu này sang loại khác:
    # Chuyển từ float sang int thì cú pháp là int(float):
print(int(1.0))
    # Ngược lại để chuyển từ float sang int thì cú pháp là float(int):
    # Tiếp nếu chuyển từ bool sang int thì cú pháp là bool(int) có hai trường hợp là 0 hoặc 1
print(bool(1))
    # Nếu một string chỉ bao gồm các số thực thì có thể chuyển sang int
 
# Biểu thức và biến
    # Biểu thức:
print(22+33)

print(22//11)
print(22/10) #: Chia 1 gạch là không làm tròn
print(22//10) #: Chia 2 gạch là làm tròn
print(type(2))    
# Biến
    # Gán biến: đặt a = 5
a = 5
print(a) # Cho ra kết quả là a = 5

    # Ví dụ công thức tính doanh thu bằng biến giá và số lượng: 
gia = 2
so_luong = 3
doanh_thu = gia*so_luong
print(doanh_thu)

# String
day_so = "1 2 3 4 5 6"
file_data = "bang doanh so"
print(file_data[0])
    # Có thể nhập một khoảng giá trị như sau: file_data[0:4]
print(file_data[0:4])
    # Có thể chọn các chỉ số chẵn: file_data[::2]
print(file_data[::2])
    # Có thể chọn các giá trị không liên tục: file_data[0:độ dài muốn chọn giá trị:2]
file_data = "bang doanh so"   
print(file_data[0:13:2])
    # Sử dụng len để biết độ dài của string
print(len(file_data))
    # \ là một ký tự đặc biệt trong string. VD: \n là xuống dòng và \t là tab
print("doanh_thu \n chi phi")
print("giuong\tngu")
    # Nếu muốn dùng dấu \ thì viết code là \\ thì python sẽ hiểu
print("%growth doanh thu = doanh thu - doanh thu(-1)\\ doanh thu (-1)")
    # Các phương thức biến đổi string: như chuyển từ chữ thường sang in hoa hoặc ngược lại, hay thêm chữ
FILE_DATA = file_data.upper() # Chuyển từ thường sang in hoa
print(FILE_DATA)

file_data = FILE_DATA.lower() # Chuyển từ in hoa sang thường
print(file_data)

print(file_data.find("b")) # Tìm kiếm từ ở vị trí số mấy trong chuỗi

file_data = file_data.replace("bang", "bao cao") # Thay thế từ: đối số thứ nhất là từ muốn thay, đối số thứ hai là thay bằng từ nào
print(file_data)

# Tuple: Gần giống như danh sách nhưng không thể thay đổi và ngăn cách với nhau bằng dấu phấy, ngoặc đơn
bang_gom = ("doanh_thu", "chi_phi", "loi_nhuan", 2025, 2024)
print(type(bang_gom))
    # Chúng ta chỉ có thể biến đổi tuple bằng cách gán nó cho biến khác
so = (10,2,3,4,5)
bang_gom_1 = sorted(so)
print(bang_gom_1)

# List: Danh sách cũng là một cấu trúc dữ liệu trong Python và biểu diễn trong dấu ngoặc vuông. Khác với tuple thì list có thể thay đổi nên tuple thường có tính bảo mật cao hơn.

doanh_so = ["a*b", "a1*b1"]
print(type(doanh_so))
doanh_so[0] = "a2*b2"
doanh_so.append("a3*b3") # dùng phương thức để thêm append cho list. Nếu là tuple thì không thể thêm hay xóa cái gì cả.
doanh_so.insert(1,"a4*b4")
doanh_so.remove("a1*b1")
print(doanh_so)

# Cả List và Tuple có thể chứa chuỗi (string), số thực (float), số nguyên (int) và tuple, thậm chí cả list khác.
# List và Tuple khác nhau nhất ở chỗ tuple không thể thay đổi hay thêm bớt còn list thì có.

# Dictionaries: từ điển: bao gồm có key và value, mỗi key sẽ gắn liền với một value
# Dictionaries nằm trong dấu ngoặc nhọn, list là ngoặc vuông, tuple là ngoặc tròn.
example_dictionaries = {"metagame" : 2021, "sonatgame" : 2020}
print(type(example_dictionaries))
print(example_dictionaries.keys())
    # Để tìm value của một key dùng method sau: 
print(example_dictionaries["metagame"])
    # Thêm một key và một value vào dictionaries như sau:
example_dictionaries["rocketstudio"] = 2015
example_dictionaries["betagame"] = 2020
print(example_dictionaries)
    # Để xóa một key và value trond dictionaries làm như sau: 
del(example_dictionaries["betagame"])
print(example_dictionaries)
    # Để xác định một key có trong dictionaries không làm như sau:
print("tripsoft" in example_dictionaries)