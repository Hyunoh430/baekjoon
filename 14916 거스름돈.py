n = int(input())
coins = [5, 2]
count = 0
if (n % 5) % 2 == 0:
    for coin in coins:
        count += n // coin
        n = n % coin

else:
    if n < 5:
        print(-1)
        exit()
    count = count + n // 5 - 1
    n = n - (5 * count)
    count = count + (n // 2)

print(count)
