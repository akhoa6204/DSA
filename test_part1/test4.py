def calculate_odd_sum(n):
    sum_result = 0
    for i in range(1, n + 1):  
        if i % 2 != 0:
            sum_result += i
    return sum_result

n_value = 100
print(calculate_odd_sum(n_value))
# 4A
