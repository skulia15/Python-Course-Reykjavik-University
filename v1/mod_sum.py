def mod_sum(n):
    sum = 0
    for x in range(0, n):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x
    return sum
