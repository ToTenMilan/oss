def calculate_payment(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance - integer
    annualInterestRate - float
    montlhyPamentRate - float

    return balance after paying minimum monthly payment, for one year
    """
    montlhyInterestRate = annualInterestRate / 12.0
    for month in range(12):
        minimumMonthlyPayment = balance * monthlyPaymentRate
        balance = balance - minimumMonthlyPayment
        balance = balance + (balance * montlhyInterestRate)
    print("Remaining balance: " + str(round(balance,2)))

# calculate_payment(42, 0.2, 0.04)
calculate_payment(484, 0.2, 0.04)
