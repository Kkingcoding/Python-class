l = list(range(0,50))

result = [x*3 for x in l if x % 2 == 0]
print(result)

result = []
for x in l:
    if x % 2 == 0:
        result.append( x * 3 )
print(result)