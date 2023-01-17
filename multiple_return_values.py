def arithmetic(num1, num2):
    add = num1+num2
    sub = num1-num2
    mult = num1*num2
    div = num1/num2
    # return the value
    return add, sub, mult, div


a, b, c, d = arithmetic(16, 4)
print("add", a)
print("sub", b)
print("mult", c)
print("div", d)
