'''
x = 6
y = 2
n = 0
h = 0.2
N = int(input("Enter number of iterations of your ODEs do you want?: "))

while n < N:
    y_prime = (1/x)*((y**2) + y)
    y += y*h
    x += h
    n += 1
    print("This is iteration " + n + ": " + str(y_prime))
'''
# The Approximation Method of Euler:
x = 6
y = 2
n = 0
h = 0.2
N = int(input('How many iterations of your diffeq do you want to do? '))
while n < N:
    y += y * h
    x += h
    n += 1
    y_prime = (1/x) * ((y**2) + y)
    print('at x = %.1f y prime equals %.6f' % (x, y_prime))