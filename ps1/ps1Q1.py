# The portion that I have to pay as part of the installment agreement
portion_down_payment = 0.25
# A counter of my savings at all time, starting at 0$.
current_savings = 0
# An annual investment rate
r = 0.04
# The annual salary I make
annual_salary = float(input("Enter your annual salary: "))
# The portion of my salary that goes for the down payment of the house
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# The total cost of a house
total_cost = float(input("Enter the cost of your dream home: "))

# Calculates the monthly salary
monthly_salary = annual_salary/12
# Looping to count the months until the needed sum is obtained, initializing the months counter
months = 0
while current_savings < total_cost * portion_down_payment:
    # First rise the current amount by the monthly rate based on what we had there during the whole month
    current_savings += current_savings * (r/12)
    # Second, at the end of the month adding the agreed portion of the monthly salary for saving and investment
    current_savings += monthly_salary * portion_saved
    # Counting another month
    months += 1
print("Number of months:", months)
