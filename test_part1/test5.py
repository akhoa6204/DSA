def test(m,n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 or i == m or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
m=5
n=4
test(m,n)
# 5A

