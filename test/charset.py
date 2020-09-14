# unicode
str = "互联网数据获取技术"
print(str)
strgbk = str.encode("gbk")
print(strgbk)
strutf8 = str.encode("utf-8")
print(strutf8)
strgb2312 = str.encode("gb2312")
print(strgb2312)
strgb2u8 = strgbk.decode("gbk").encode("utf-8")
print(strgb2u8)
print(strgb2u8.decode("utf-8"))