def tribonacci(signature, n):
    result = signature
    for i in range(3,n):
        result += [result[i-3] + result[i-2] + result[i-1]]
    return result[0:n]
