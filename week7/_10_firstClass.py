func = mul
func
def ret_func(a):
    return lambda x : 2 * 3

ret = ret_func(3)
print(ret)
print(ret(3))

def mul_mul(f,a):
    return f(a) * f(a)

ret = mul_mul(mul,4)
print(ret)
