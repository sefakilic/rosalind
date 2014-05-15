

masses = [57, 71, 87, 97, 99, 101, 103, 113, 113, 114,
          115, 128, 128, 129, 131, 137, 147, 156, 163, 186]

memo = dict()

def spectrum(n, xs):
    global memo
    if n < 0:
        memo[n] = 0
    elif (n == 0):
        memo[n] = 1
    if n not in memo:
        memo[n] = sum(map(lambda x: spectrum(n-x, xs), xs))
    return memo[n]
                
