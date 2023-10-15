import random

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            # 1부터 100까지의 랜덤한 정수로 행렬 A의 원소를 초기화
            row.append(random.randint(1, 100))
        matrix.append(row)
    return matrix

def mul_matrix(a, b):
    result = []
    for i in range(len(a)):
        row_result = []
        for j in range(len(b[0])):
            element_sum = 0
            for k in range(len(b)):
                element_sum += a[i][k] * b[k][j]
            row_result.append(element_sum)
        result.append(row_result)
    return result

N = int(input("행렬의 크기 N을 입력하세요: "))
A = create_matrix(N)
result = mul_matrix(A, A)

print("\n행렬 A:")
for row in [A]:
    print('\n'.join(map(str, row)))

print("\n행렬 A * A 결과:")
for row in [result]:
    print('\n'.join(map(str,row)))
