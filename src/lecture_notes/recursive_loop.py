def hello(n, result):
    if n == 0:
        return result

    return hello(n - 1, result + [n])
    

result = hello(10, [])

print(result)
