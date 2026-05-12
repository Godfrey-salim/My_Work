# This code demonstrates how to handle exceptions in Python when calculating total income based on tax and income inputs from the user.
try:
    tax = float(input("Enter your tax: "))
    income = float(input("Enter your income: "))
    total_income = income / tax
    print("Your total_income is: ", total_income)
# The following exceptions are handled:
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Tax cannot be zero.")