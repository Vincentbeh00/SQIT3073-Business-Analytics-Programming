#Function to calculate Debt Service Ratio (DSR)
def calculate_DSR(housing_loan, monthly_income, other_commitments):
    total_commitments = housing_loan + other_commitments
    DSR = (total_commitments/monthly_income)*100
    return DSR
