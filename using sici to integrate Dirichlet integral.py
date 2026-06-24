from scipy.special import sici
import numpy as np

# Compare for finite x
x_vals = [1, 10, 100, 1000]
for x in x_vals:
    si, ci = sici(x)
    print(f"Si({x:4d}) = {si:.8f}")

# Si(∞) = π/2 exactly
print(f"\nSi(∞) = {sici(np.inf)[0]} = π/2? {np.isclose(sici(np.inf)[0], np.pi/2)}")

print("Analytical value (π/2):", np.pi/2)