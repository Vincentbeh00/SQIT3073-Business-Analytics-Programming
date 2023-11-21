#Function to calculate monthly instalment 
def monthly_instalment_calc (principal, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = loan_term*12
    monthly_payment = (principal*monthly_interest_rate) / (1-(1+monthly_interest_rate)** -num_payments)
    return monthly_payment


#Function to calculate total amount payable
def total_payment_calc (monthly_payment, loan_term):
    return monthly_payment*loan_term*12
    