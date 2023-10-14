pin = input("주민등록 번호: ")

yymmdd = pin[:6]
num = pin[7:]

print("앞자리: " + yymmdd)
print("뒷자리: " + num)