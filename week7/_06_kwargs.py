def kwargs_sample(a,b,**kwargs):
    print(type(kwargs))
    return kwargs.items()

l_1 = kwargs_sample(a=1,b=2,c=3,d=4,e=5,f=6)
print(l_1)

l_2 = kwargs_sample(1,2,c=3,d=4,e=5,f=6)
print(l_2)

#함수의 필수 인자와 옵션인자를 구분해서 처리 할 수 있음