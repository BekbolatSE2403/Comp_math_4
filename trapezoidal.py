def trapezoidal_rule(f, a, b, n):

    # Step 1: Calculate step size
    h = (b - a) / n
    
    # Step 2: Add endpoints (f(a) + f(b))
    total = f(a) + f(b)
    
    # Step 3: Add interior points (each counted twice)
    for i in range(1, n):
        x_i = a + i * h
        total += 2 * f(x_i)
    
    # Step 4: Multiply by h/2
    return (h / 2) * total

# Example usage:
def example_trapezoidal():
    f = lambda x: x**2  # Function: f(x) = x^2
    a, b = 0, 2         # Interval [0, 2]
    n = 4               # 4 trapezoids
    
    result = trapezoidal_rule(f, a, b, n)
    exact = 8/3         # ∫x^2 dx from 0 to 2 = 8/3 ≈ 2.6667
    
    print(f"Trapezoidal Rule (n={n}): {result:.6f}")
    print(f"Exact value: {exact:.6f}")
    print(f"Error: {abs(result-exact):.6f}")

example_trapezoidal()