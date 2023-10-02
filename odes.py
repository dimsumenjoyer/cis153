# Euler's Approximation for Differential Equations
x = 6
y = 2
n = 0
h = 0.2
N = int(input("How many iterations of your diffeq do you want to do?: "))
while n < N:
    x += h
    n += 1
    y_prime = (1/x) * ((y**2) + y)
    y += h*y_prime
    print(f"At {n} iteration(s) at x = %.1f, y = %.5f." % (x, y))
