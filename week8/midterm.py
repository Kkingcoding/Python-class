print("★ Welocome! 정수 입/출력 프로그램입니다 ★")
def menu():                                     #필요 시 보여줄 메뉴 함수로 선언
    print("\n1 : 정수 입력하기")
    print("2 : 제일 먼저 입력된 정수 꺼내기")
    print("3 : 저장된 정수 모두 보여주기")
    print("4 : 저장된 정수 중 중복 제거하고 보여주기")
    print("5 : 프로그램 종료\n")

num_list = []                                   #빈 리스트 생성
menu()                                          #메뉴 처음에만 보여줌
while True:
    choice = input("메뉴 번호를 입력하세요 : ")     #메뉴 입력 반복
    if choice == '1':
        while True:
            num = input("정수를 입력하세요 : ")
            try:
                num_int = int(num)
                num_list.append(num_int)
                break
            except ValueError:                  #입력 받은 값 예외 처리
                print(f"{num}은 정수가 아닙니다.")

    elif choice == '2':
        if num_list:
            print(f"{num_list[0]}을 삭제했습니다.")
            del num_list[0]                     #완전히 삭제
        else:                                   #리스트 비어 있을 시 예외 처리
            print("입력된 정수가 없습니다.")

    elif choice == '3':
        if num_list:
            print("저장된 숫자는 : ",','.join(map(str,num_list)))
        else:
            print("입력된 정수가 없습니다.")

    elif choice == '4':
        unique_nums = list(set(num_list))
        if num_list:
            print("중복 제거한 값은 : ",','.join(map(str,unique_nums)))
                                                #일시적인 제거
        else:
            print("입력된 정수가 없습니다.")

    elif choice == '5':
        print("프로그램을 종료합니다.")
        break

    else:                                       #입력 받은 메뉴 번호 예외 처리
        print("1~5번 메뉴만 입력하세요.")
        choice = menu()                         #메뉴 다시 보여줌