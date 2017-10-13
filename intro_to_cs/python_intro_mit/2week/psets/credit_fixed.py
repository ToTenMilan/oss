def calculateYearlyPayment(balance, annualInterestRate, monthlyPayment):
  """
  balance - integer
  annualInterestRate - float
  montlhyPamentRate - float

  return balance after paying minimum monthly payment, for one year
  """
  monthlyInterestRate = annualInterestRate / 12.0
  unpaidBalance = 0
  for month in range(12):
      # minimumMonthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + (unpaidBalance * monthlyInterestRate)
  return balance

def calculateLowestBalance(balance, annualInterestRate):
  payment = 0
  index = 0
  amountToPay = 1
  while amountToPay >= 0:
    index += 1
    payment += 0.01
    amountToPay = calculateYearlyPayment(balance, annualInterestRate, payment)
    # print(balance)
  print("Lowest Payment: " + str(payment))

balance = 500000
annualInterestRate = 0.2
calculateLowestBalance(balance, annualInterestRate)


