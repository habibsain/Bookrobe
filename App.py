price = 1000000
buyer_has_good_credit = input('Do you have good credit? answer "True" or "False"\n')
if buyer_has_good_credit == "True":
    downpayment = 0.2 * price
    print(f'Downpayment required is ${downpayment}')

elif buyer_has_good_credit == "False":
    downpayment = 0.1 * price
    print(f'Downpayment required is ${downpayment}')
else:
    print("Invalid input")

