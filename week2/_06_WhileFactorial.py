# 사용자로부터 양의 정수를 입력받음
num = int(input("양의 정수를 입력하세요: "))

# 초기값 설정
factorial = 1
current_number = 1

# while 루프를 사용하여 팩토리얼 계산
while current_number <= num:
    factorial *= current_number
    current_number += 1

# 결과 출력
print(f"{num}의 팩토리얼은 {factorial}입니다.")