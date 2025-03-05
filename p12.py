def is_perfect_square(x):
    return int(x**0.5)**2 == x

print(is_perfect_square(16))  # True
print(is_perfect_square(14))  # False
