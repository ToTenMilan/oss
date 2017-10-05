balance = 320000
annualInterestRate = 0.2

# balance = 999999
# annualInterestRate = 0.18

guessed = False
monthlyInterestRate = annualInterestRate / 12.0
lowBound = balance / 12
highBound = (balance * ( 1 + monthlyInterestRate) ** 12) / 12.0
payment = (lowBound + highBound) / 2
# payment = 0

while guessed == False:

    # print(payment)
    if (balance * ( 1 + monthlyInterestRate) ** 12) - (payment * 12) > 0.0:
        highBound = payment
        payment = (lowBound + highBound) // 2
        print("lowBound: "); print(lowBound)
    elif (balance * ( 1 + monthlyInterestRate) ** 12) - (payment * 12) < 0.0:
        lowBound = payment
        payment = (lowBound + highBound) // 2
        print("highBound: "); print(highBound)
    elif (balance * ( 1 + monthlyInterestRate) ** 12) - (payment * 12) == 0:
        print("Lowest Payment: " + str(round(payment, 2)))
        guessed = True

