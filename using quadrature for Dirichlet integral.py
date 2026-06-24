from scipy.integrate import quad
import numpy as np

result, err = quad(lambda x: np.sin(x)/x, 0, np.inf, 
                   epsrel=1e-8, limit=1000)
print("Numerical integral:", result)
print("Analytical value (π/2):", np.pi/2)
print("Difference:", abs(result - np.pi/2))