# from IPython.display import clear_output

class Calculator():
    def __init__(self,incomes,expenses,cashflows,rois):
        self.incomes=incomes
        self.expenses=expenses
        self.cashflows=cashflows
        self.rois=rois
    def income(self):
        # clear_output()
        rental_income = int(input("What's your Rental Income? "))
        # if rental_income != int():
        #     return ROICalculator.income()
        laundry_income = int(input("Income from laudry machines? "))
        miscellaneous_income = int(input("Any miscellaneous income (i.e. storage)? "))
        income_total = rental_income + laundry_income + miscellaneous_income
        print(f'your total RENTAL INCOME is: ${income_total}')
        self.incomes = income_total
        # self.incomes.append(income_total)
    def expense(self):
        expense_tax = int(input("How much will pay in taxes monthly? "))
        expense_insurance = int(input("Monthly Insurance expenses? "))
        print("Will you be responsible for any of the utilities (electic,water,sewer,gas):")
        expense_utilities = input("If you're paying ANY of these, type 'yes'. If the renter will be paying ALL the expenses type 'no'.  ")
        if expense_utilities.lower() == "yes":
            expense_electric = int(input("What are the monthly ELECTRIC expenses? "))
            expense_water =int(input("What are the monthly WATER expenses? "))
            expense_sewer = int(input("What are the monthly SEWER expenses? "))
            expense_gas = int(input("What are the monthly WATER expenses? "))
            total_utilities = expense_electric + expense_water + expense_sewer + expense_gas
            print(f"\nYour total monthly utility expenses are: ${total_utilities}")
        else:
            total_utilities = 0
            print("Great!!  You don't have any utility expenses.")
        print("\n I still have a few more monthly expense questions.")
        expense_hoa = int(input("What are the HOA expenses? "))
        expense_lawn_snow = int(input("what are the LAWN/SNOW care/removal expenses? "))
        expense_vacancy = int(input('What is your monthly "rainy day" VACANCY fund contribution? '))
        expense_repairs = int(input("What are the your monthly REPAIRS expenses? "))
        expense_capex = int(input("What are your average monthly CAPTIAL EXPENDITURES (CAPEX) (eg new roof)? "))
        expense_propertymanagement = int(input("How much will you be paying a PROPERTY MANAGEMENT company every month? "))
        expense_mortgage = int(input("Lastly, What's your monthly mortgage? "))
        expense_total = expense_tax + expense_insurance + total_utilities + expense_hoa + expense_lawn_snow + expense_vacancy + expense_repairs + expense_capex + expense_propertymanagement + expense_mortgage
        self.expenses = expense_total
        # self.expenses.append(expense_total)
        print(f'Your Total EXPENSES are: ${expense_total}')
    def cashflow(self):
        # Total Cash Flow = Total Income - Total Expenses
        self.cashflows = self.incomes - self.expenses
        total_cashflow = self.cashflows
        # for i in range (len(self.incomes)):
        #     self.cashflows = self.incomes[i] - self.expenses[i]
        print("Based on the information you've given us,")
        print(f"Your Total MONTHLY CASH FLOW is: ${total_cashflow}")
    def roi(self):
        roi_downpayment = int(input("What's your total DOWN PAYMENT? "))
        roi_closingcost = int(input("What are your CLOSING COSTS? "))
        roi_rehabbudget = int(input("What's your total REHAB BUDGET (inital costs to fix unit before renting)? "))
        roi_miscother = int(input("Lastly, How much in MISCELLANEOUS expeneses? "))
        total_investment = roi_downpayment + roi_closingcost + roi_rehabbudget + roi_miscother
        print(f"Your INVESTMENT Total is: ${total_investment}")
        # CALCULATE ANNUAL CASH FLOW:
        annual_total_flow = self.cashflows * 12
        # COMPUTE ROI: Annual cash flow / Total Investment
        self.rois = (annual_total_flow/total_investment)*100
        rois = self.rois
        print(f"\n\n\nYour Total Cash on Cash ROI is: {rois}%")

ROICalculator = Calculator([],[],[],[])  #INSTANTIATING here

# The function below will run the ROICalculation(Calculator) methods

def run():
    while True:
        print("\n\nWelcome to the Rental Property Return on Investment (ROI) Calculator")
        print("\n To calculate your ROI, we'll need to ask you a series a questions about your rental property.")
        response = input("To begin, please type 'income'. Or, if you'd rather leave, type 'quit'.  ")
        if response.lower() == 'quit':
            print("Thanks for stoping by")
            break
        if response.lower() == 'income':
            print("The 1st step is to establish your MONTHLY Total Rental Income? ")
            ROICalculator.income()
            print("\nStep #2 is to establish your MONTHLY Total Expenses? ")
            ROICalculator.expense()
            print("\nStep #3 is to now calculate your MONTHLY cash flow.")
            ROICalculator.cashflow()
            print("\n\nStep #4 is the last step to calculat the ROI.")
            ROICalculator.roi()

run()