import math

def dirichlet_integral(n=100000, limit=100.0):
    # Integrate from 0 to limit and double it (even function, skip x=0 singularity)
    a = 0.0
    b = limit
    h = (b - a) / n
    integral = 0.0  # sin(0)/0 is handled as limit=1
    
    for i in range(1, n):          # start from 1 to avoid x=0
        x = a + i * h
        integral += math.sin(x) / x
    
    # Add endpoints (left endpoint contribution ≈ 1)
    integral += 0.5 * (1.0 + math.sin(b) / b)
    return 2 * integral * h       # double for full -inf to inf

result = dirichlet_integral()
print("Numerical integral:", result)
print("Analytical value (π):", math.pi)