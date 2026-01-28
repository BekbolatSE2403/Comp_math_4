def booles_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4 for Boole's rule")
    
    h = (b - a) / n
    total = 0
    
    # Apply weights according to Boole's rule pattern
    for i in range(n + 1):  # n+1 points total
        x_i = a + i * h
        
        if i == 0 or i == n:  # Endpoints
            weight = 7
        elif i % 2 == 1:      # Odd indices
            weight = 32
        elif i % 4 == 2:      # Even indices not divisible by 4
            weight = 12
        else:                 # Even indices divisible by 4
            weight = 14
        
        total += weight * f(x_i)
    
    return (2 * h / 45) * total

# Example usage:
def example_booles():
    f = lambda x: x**4  # Function: f(x) = x^4
    a, b = 0, 4         # Interval [0, 4]
    n = 4               # Must be multiple of 4
    
    result = booles_rule(f, a, b, n)
    exact = 1024/5      # ∫x^4 dx from 0 to 4 = 1024/5 = 204.8
    
    print(f"Boole's Rule (n={n}): {result:.6f}")
    print(f"Exact value: {exact:.6f}")
    print(f"Error: {abs(result-exact):.6f}")
    print("Note: For x^4, Boole's rule gives exact result!")

example_booles()