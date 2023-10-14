print("숫자를 입력하세요: ") 
x = input()
print("입력받은 값의 자료형은 " + str(type(x))+ "입니다.")

#입력받은 값을 정수로 변환
x = int(x)
print("캐스팅 이후 값은 %d이고, 자료형은 %s입니다." % (x,type(x)))