n = int(input())
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
arr = []
for i in range(2, n + 2):
    if is_prime(i):
        arr.append("1")
    else:
        arr.append("2")
print(len(set(arr)))
print(" ".join(arr))