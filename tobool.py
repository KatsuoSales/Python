# 檔案名稱： tobool.py
# 檔案說明： 強制轉換成布林值
# -----------------------------

# 設定整數變數與變數值
int1 = 3
int2 = 0
int3 = -4

# 設定浮點數變數與變數值
flt1 = 3.2
flt2 = 3.9
flt3 = 0.0
flt4 = -4.3
flt5 = -4.9

# 設定字串變數與變數值
str1 = "4"
str2 = "3.2"
str3 = "0"
str4 = "0.0"
str5 = "-3"
str6 = "-5.2"
str7 = "Happy"


# 將整數轉換成布林值
int2bool1 = bool(int1)  # int1 = 3
int2bool2 = bool(int2)  # int2 = 0
int2bool3 = bool(int3)  # int3 = -4

# 將浮點數轉換成布林值
flt2bool1 = bool(flt1)  # flt1 = 3.2
flt2bool2 = bool(flt2)  # flt2 = 3.9
flt2bool3 = bool(flt3)  # flt3 = 0.0
flt2bool4 = bool(flt4)  # flt4 = -4.3
flt2bool5 = bool(flt5)  # flt5 = -4.9

# 將字串轉換成布林值
str2bool1 = bool(str1)  # str1 = "4"
str2bool2 = bool(str2)  # str2 = "3.2"
str2bool3 = bool(str3)  # str3 = "0"
str2bool4 = bool(str4)  # str4 = "0.0"
str2bool5 = bool(str5)  # str5 = "-3"
str2bool6 = bool(str6)  # str6 = "-5.2"
str2bool7 = bool(str7)  # str7 = "Happy"


#  顯示整數轉換成布林值結果
print(int2bool1)
print(int2bool2)
print(int2bool3)

#  顯示浮點數轉換成布林值結果
print(flt2bool1)
print(flt2bool2)
print(flt2bool3)
print(flt2bool4)
print(flt2bool5)

#  顯示字串轉換成布林值結果
print(str2bool1)
print(str2bool2)
print(str2bool3)
print(str2bool4)
print(str2bool5)
print(str2bool6)
print(str2bool7)
