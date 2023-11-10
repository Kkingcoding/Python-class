marks = [("1",90), ("2", 25), ("3", 67), ("4", 45), ("5",80)]

for name, score in marks:
    print(f"{score = }")
    if score >= 60:
        print(f"{name}합격입니다.\n")
    else:
        print(f"{name} 불합격입니다\n")