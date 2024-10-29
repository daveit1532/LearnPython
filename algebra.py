from sympy import symbols, Eq, solve

# Define variables
x, y = symbols('x y')

# Create an equation
equation = Eq(x + y, 10)

# Solve the equation for x
solution = solve(equation, x)
print("Solution for x:", solution)
