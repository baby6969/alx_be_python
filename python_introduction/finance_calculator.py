<<<<<<< HEAD
monthly_income = float (input("Enter your monthly income: "))
monthly_expenses = float (input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
Projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
=======
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = (monthly_income - monthly_expenses)
Projected_Savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
>>>>>>> 02028c1 (Save local changes before rebase)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")
