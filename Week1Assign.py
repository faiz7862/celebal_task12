def lower_triangle(n):
    for i in range(1, n + 1):
        print('* ' * i)

def upper_triangle(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

n = int(input("Enter the size of pattern:"))
print("Lower traingle Pattern")
lower_triangle(n)
print("\nUpper traingle Pattern")
upper_triangle(n)
print("\nPyramid Pattern")
pyramid(n)
