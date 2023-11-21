import os,platform
import Modules.DSR as debt_service_calc
import Modules.HLC as housing_loan_calc
import pickle

#Function to clear screen 
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Function to display menu options
def menu():
    print ("\nMenu:")
    print ("1. Calculate New Loan")
    print ("2. Display All Previous Loan Calculations")
    print ("3. Modify DSR Threshold")
    print ("4. Exit Program")

#Function to validate and retrieve a float value within limits
def float_validation(prompt, lower_limit=None, upper_limit=None):
    while True:
        try:
            value = float(input(prompt))
            if lower_limit is not None and value < lower_limit:
                raise ValueError("Input is below the minimum limit.")
            if upper_limit is not None and value > upper_limit:
                raise ValueError("Input is above the maximum limit.")
            return value
        except ValueError as e: 
            if "maximum limit" in str(e):
                print(f"Invalid input, the value cannot exceed {upper_limit}.")
            else:
                print(f"Invalid input, please enter a valid numerical value")

#Function to validate and retrieve an integer value within limits
def int_validation(prompt, lower_limit =None):
    while True: 
        try:
            value = int(input(prompt))
            if lower_limit is not None and value < lower_limit:
                raise ValueError("Input is below the minimum limit.")
            return value
        except ValueError as e:
            print(f"Invalid input, {e} please enter a valid year for loan term.")

#Function to adjust the Debt Service Ratio (DSR) threshold
def adjust_dsr_threshold():
    global eligible_dsr
    new_threshold = float_validation("Enter the new eligible DSR threshold in %: ", lower_limit=0, upper_limit=85)
    eligible_dsr = new_threshold
    print (f"New threshold @{eligible_dsr:.2f}% is saved.")

#Function to save loan details to a file using pickle
def save_loan(loan_details):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'loan_calculations.pkl')
    with open(file_path, 'wb') as file:
        return pickle.dump(loan_details, file)

#Function to load loan details from a file using pickle  
def load_loan_details():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'loan_calculations.pkl')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    else:
        return []
    
#Main function to execute the loan calculation program
def main():
    clear_screen() #clear screen at the start
    global eligible_dsr
    eligible_dsr = 70 #default eligible dsr

    loan_details = load_loan_details() #load existing loan details if available

    while True:
        menu() #display the menu options
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            #Code to calculate a new loan, validate inputs, and append loan details to the list
            principal = float_validation("Enter the principal loan amount: ", lower_limit=100000)
            opr = float_validation("Enter the current Overnight Policy Rate (OPR) %: " ,lower_limit=0)
            base_rate = float_validation("Enter the loan base rate %: " ,lower_limit=0)
            annual_interest_rate = opr+base_rate
            loan_term = int_validation("Enter the loan term in years: ", lower_limit=1)
            monthly_income = float_validation("Enter the applicant's monthly income: ", lower_limit=2000)
            other_commitments = float_validation("Enter the applicant's other monthly commitments: ", lower_limit=0)

            monthly_payment = housing_loan_calc.monthly_instalment_calc(principal, annual_interest_rate, loan_term)
            total_payment = housing_loan_calc.total_payment_calc(monthly_payment, loan_term)
            dsr = debt_service_calc.calculate_DSR(monthly_payment, monthly_income, other_commitments)


            loan_eligibility = "Eligible" if dsr <= eligible_dsr else "Not Eligible"

            print("\nLoan Details:")
            print(f"Principal Loan: RM{principal:.2f}")
            print(f"Monthly Instalment: RM{monthly_payment:.2f}")
            print(f"Total Payment: RM{total_payment:.2f}")
            print(f"Debt Service Ratio (DSR): {dsr:.2f}%")
            print(f"DSR Threshold: {eligible_dsr:.2f}%")
            print(f"Eligibility: {loan_eligibility}")

            loan_details.append({
                'Principal': f'RM{principal:.2f}',
                'Annual Interest Rate': f'{annual_interest_rate:.2f}%',
                'Loan Term': f'{loan_term} years',
                'Monthly Income': f'RM{monthly_income:.2f}',
                'Other Commitments': f'RM{other_commitments:.2f}',
                'Monthly Payment': f'RM{monthly_payment:.2f}',
                'Total Payment': f'RM{total_payment:.2f}',
                'DSR': f'{dsr:.2f}%',
                'DSR Threshold': f'{eligible_dsr:.2f}%',  # Add DSR needed for each loan
                'Eligibility': loan_eligibility,
            })
            save_loan(loan_details)

        elif choice == '2':
             #Code to display previous loan calculations and allow deletion of a calculation
            if not loan_details:
                print("No previous loan calculations.")
            else:
                print("\nPrevious Loan Calculations: ")
                for idx, details in enumerate(loan_details, start =1):
                    print (f"\nCalculation {idx}:")
                    for key,value in details.items():
                        print (f"{key}: {value}")
            
            #Loan Detail Deletion option for user
                delete_choice = input("\nWould you like to delete a calculation? Enter the calculation number to delete (0 to cancel): ")
                if delete_choice.isdigit():
                    delete_index = int(delete_choice)
                    if delete_index > 0 and delete_index <= len(loan_details):
                        deleted_calculation = loan_details.pop(delete_index - 1)
                        print(f"\nCalculation {delete_index} deleted.")
                        save_loan(loan_details)
                    elif delete_index == 0:
                        print("Deletion cancelled.")
                    else:
                        print ("Invalid Calculation number. No changes made.")
                else:
                    print("Invalid input, please enter a number.")

        elif choice == '3':
             #Code to modify the DSR threshold
            print("\nCurrent Debt Service Ratio Threshhold is " + str(eligible_dsr) + "%")
            adjust_dsr_threshold()

        elif choice == '4':
            #Code to exit the program
            confirm_exit = input("\nAre you sure you want to exit? (y/n): ").lower()

            if confirm_exit == 'y':
                print ("Exiting Program. Goodbye!\n")
                break
            elif confirm_exit == 'n':
                #continue the loop, return to the menu
                print ("\nRedirecting to menu.")
                continue

            else:
                print ("\nInvalid choice, returning to the menu")

        else: 
            print("\nInvalid choice. Please enter a number between 1 and 4 only.")

main()