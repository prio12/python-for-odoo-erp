
# Python Fundamentals: Variables and Basic Output
# Learning project: Python for Odoo and ERP

# 1. Assigning values to variables
product_name = "Wireless Mouse"
stock = 12
price = 2000.00
is_available = True

print("=== Product Information ===")
print(product_name)
print(stock)
print(price)
print(is_available)

# 2. Using variables in readable output
print(f"Product: {product_name}")
print(f"Stock: {stock}")
print(f"Price: BDT {price:.2f}")

# 3. Numbers and strings behave differently
quantity = 5
print(quantity + quantity)  # Numeric addition: 10

code = "12"
print(code + code)  # String concatenation: 1212

# 4. Converting a numeric string to an integer
numeric_stock = int("12")
print(numeric_stock + 3)  # Output: 15

# 5. Updating a variable
stock = 10
print(f"Updated stock: {stock}")

# 6. Python variable names are case-sensitive
product_name = "Wireless Mouse"
print(product_name)  # Correct variable name
