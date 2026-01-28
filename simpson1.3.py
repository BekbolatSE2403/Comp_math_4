def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n
    
    # Start with endpoints
    total = f(a) + f(b)
    
    # Add interior points with weights 4 (odd) and 2 (even)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 1:  # Odd index
            total += 4 * f(x_i)
        else:           # Even index
            total += 2 * f(x_i)
    
    return (h / 3) * total

# Example usage:
def example_simpson_13():
    f = lambda x: x**2  # Function: f(x) = x^2
    a, b = 0, 2         # Interval [0, 2]
    n = 4               # Must be even: 4 subintervals = 5 points
    
    result = simpson_one_third(f, a, b, n)
    exact = 8/3         # ∫x^2 dx from 0 to 2 = 8/3 ≈ 2.6667
    
    print(f"Simpson's 1/3 Rule (n={n}): {result:.6f}")
    print(f"Exact value: {exact:.6f}")
    print(f"Error: {abs(result-exact):.6f}")
    print("Note: For x^2, Simpson's 1/3 gives exact result!")

example_simpson_13()