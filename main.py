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
    "savings" : 0.0,
    "mortgage/rent" : 0.0,
    "groceries" : 0.0,
    "vehicle loan(s)" :0.0,
    "vehicle insurance" : 0.0,
    "health insurance" : 0.0,
    "clothes" : 0.0,
    "entertainment" : 0.0,
    }