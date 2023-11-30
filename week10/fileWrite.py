f = open("new_file.txt",'w')

for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data) #data를 파일 객체 f에 써라.
f.close()