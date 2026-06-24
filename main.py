# ==============================================================================
# MILESTONE 1: CORE MATH ENGINE BLUEPRINT
# ==============================================================================
# 1. Define the budget categories data structure and assign target percentages.
# 2. Add a safety check to ensure all percentages add up to exactly 100% (1.0).
# 3. Prompt the user in the terminal to manually type in a single deposit amount.
# 4. Loop through each category and calculate its exact calculated cash split.
# 5. Handle any fractional rounding errors so the total matches down to the penny.
# 6. Print a clean, readable text summary of the results to the terminal window.
# ==============================================================================
budget_categories = {
    "savings" : 0.20,
    "mortgage/rent" : 0.30,
    "groceries" : 0.15,
    "vehicle loan(s)" :0.10,
    "vehicle insurance" : 0.05,
    "health insurance" : 0.10,
    "clothes" : 0.05,
    "entertainment" : 0.05,
    "unallocated" : 0.0,
    }

total_percentage = sum(budget_categories.values())

if total_percentage > 1.0:
    print(f"Total percentage is {total_percentage * 100}% this is greater than 100%. Please adjust.")
    exit()
elif total_percentage < 1.0:
    print(f"Total percentage is {total_percentage * 100}% Do you want the remaining funds to go to Unallocated")
    exit()
else:
    print("Safety check passed: Budget allocation equals 100%")

prompt = "Please enter a deposit amount."
prompt += "Example: 1000 0r 1000.25. "

while True:
    deposit_amount = input(prompt)

    try:
        clean_deposit = (deposit_amount).replace("$","").replace(",","")
        
        valid_deposit = float(clean_deposit)
        if valid_deposit <= 0:
            print("Deposit amount cannot $0 or less. Please enter and valid amount.")
            continue
        
        print(f"Success! The amount you enter is {valid_deposit}.")
        break

    except ValueError:
        print("Please enter a valid number")

    except Exception as e:
        print(f"An unexpected error ocurred {e}.")
    
for category, percentage in budget_categories.items():
    print(f"{category.title()}: Percentage in dollars: ${percentage * valid_deposit:,.2f}")