# №3. Вычисление максимального простого делителя.
num = 600851475143


def Simple(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

n = num
i = 1
while n != 1:
    i += 1
    if Simple(i) is True and n % i == 0:
        n = n / i


print(i)