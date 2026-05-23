import math
def prime_generator():
    num = 2
    while True:
        # Предполагаем, что число простое
        is_prime = True
        # Проверяем делители от 2 до корня из num
        # Если num составное, то один из множителей <= sqrt(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

gen = prime_generator()
for _ in range(20):
    print(next(gen))
