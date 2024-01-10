def check_even_odd(numbers):
    for number in numbers:
        if int(number) % 2 == 0:
            print("Even",end=" ")
        else:
            print("Odd",end=" ")

numbers = input().split()
check_even_odd(numbers)
# 3D