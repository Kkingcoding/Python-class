all = range(1,1001)
even = []
even_total = 0

for i in all:
    if i % 2 == 0:
        even.append(i)
        even_total += i

print(f"짝수 목록 : {even}"
      f"\n짝수의 합 : {even_total}")
