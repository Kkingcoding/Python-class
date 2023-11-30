f = open("new_file.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()