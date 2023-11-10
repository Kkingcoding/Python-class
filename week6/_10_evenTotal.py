even = {x for x in range(1,1001) if x % 2 == 0}
even_total = sum(even)

print(f"""짝수: {even}
짝수의 합 : {even_total}
""")

even = range(2,1001,2)
even_total = sum(even)

print(f"""짝수: {list(even)}
짝수의 합 : {even_total}""")