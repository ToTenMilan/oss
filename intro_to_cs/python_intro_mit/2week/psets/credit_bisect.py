balance = 3200
annualInterestRate = 0.2

# balance = 999999
# annualInterestRate = 0.18

guessed = False
monthlyInterestRate = annualInterestRate / 12.0
lowBound = balance / 12
highBound = (balance * ( 1 + monthlyInterestRate) ** 12) / 12.0
payment = (lowBound + highBound) / 2.0
# payment = 0



while guessed == False:
    # condition = (balance * (1 + monthlyInterestRate) ** 12) - (payment * 12)
    # condition = (balance + (balance * annualInterestRate)) - (payment * 12)
    # print(payment)
    if payment < -0.01:
        lowBound = payment
        payment = (lowBound + highBound) / 2.0
        print("lowBound: "); print(lowBound)
    elif payment > 0.01:
        highBound = payment
        payment = (lowBound + highBound) / 2.0
        print("highBound: "); print(highBound)
    elif payment >= -0.01 or payment <= 0.01:
        print("Lowest Payment: " + str(round(payment, 2)))
        guessed = True

