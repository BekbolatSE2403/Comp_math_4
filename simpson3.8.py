def simpson_three_eighth(f, a, b, n):

    if n % 3 != 0:
        raise ValueError("n must be divisible by 3 for Simpson's 3/8 rule")
    
    h = (b - a) / n
    
    # Start with endpoints
    total = f(a) + f(b)
    
    # Add interior points with weights 3 or 2
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:  # Points at multiples of 3
            total += 2 * f(x_i)
        else:           # Other points
            total += 3 * f(x_i)
    
    return (3 * h / 8) * total

# Example usage:
def example_simpson_38():
    f = lambda x: x**3  # Function: f(x) = x^3
    a, b = 0, 3         # Interval [0, 3]
    n = 3               # Must be divisible by 3: 3 subintervals = 4 points
    
    result = simpson_three_eighth(f, a, b, n)
    exact = 81/4        # ∫x^3 dx from 0 to 3 = 81/4 = 20.25
    
    print(f"Simpson's 3/8 Rule (n={n}): {result:.6f}")
    print(f"Exact value: {exact:.6f}")
    print(f"Error: {abs(result-exact):.6f}")
    print("Note: For x^3, Simpson's 3/8 gives exact result!")

example_simpson_38()