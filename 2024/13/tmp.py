from sympy import symbols, Eq, solve

# Define variables
x, y = symbols("x y")
c1, c2, c3, d1, d2, d3 = (
    94,
    22,
    8400,
    34,
    67,
    5400,
)  # Substitute your constants directly

# Define equations with constants
eq1 = Eq(x * c1 + y * c2, c3)
eq2 = Eq(x * d1 + y * d2, d3)

# Solve for x and y
solution = solve((eq1, eq2), (x, y))

# Extract values of x and y
x_val = solution[x]
y_val = solution[y]

# Minimize x + y
min_value = x_val + y_val

solvable = min_value % 1 == 0

# Display results
print("Solution for x and y:", solution)
print("Minimized value of x + y:", min_value % 1 == 0)
