import math

def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6 for Weddle's rule")
    
    h = (b - a) / n
    total = 0
    
    # Apply weights according to Weddle's pattern
    for i in range(n + 1):  # n+1 points total
        x_i = a + i * h
        
        if i == 0 or i == n:  # Endpoints
            weight = 1
        elif i % 6 == 3:      # Every 3rd point (3, 9, 15, ...)
            weight = 6
        elif i % 2 == 1:      # Other odd indices
            weight = 5
        else:                 # Even indices
            weight = 1
        
        total += weight * f(x_i)
    
    return (3 * h / 10) * total

# Example usage:
def example_weddle():
    f = lambda x: math.sin(x)  # Function: f(x) = sin(x)
    a, b = 0, math.pi          # Interval [0, π]
    n = 6                      # Must be multiple of 6
    
    result = weddles_rule(f, a, b, n)
    exact = 2.0                # ∫sin(x) dx from 0 to π = 2
    
    print(f"Weddle's Rule (n={n}): {result:.6f}")
    print(f"Exact value: {exact:.6f}")
    print(f"Error: {abs(result-exact):.6f}")
    
example_weddle()