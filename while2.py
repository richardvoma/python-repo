# conditions:print even and odd numbers between 1 to the entered number
num = 50
while num > 0:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num = num-1
