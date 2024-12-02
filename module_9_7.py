def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        i = sum(args)
        for j in range(2, i - 1):
            if (i % j) == 0:
                print('Простое')
                break
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
