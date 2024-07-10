import sys
con = 277.66
usdamount = 0
currency = input("For PKR to USD enter 'PKR' or 'USD' for USD to PKR --> ")



def pkrtousd(pkr):

    usdamount = pkr // con
    print("PKR", pkr, "in usd is: USD", usdamount)

def usdtopkr(usd):
    
    pkramount = usd * con
    pkramount = round(pkramount)
    print("USD", usd, "in pkr is: PKR", pkramount)

if currency == 'PKR' or currency == 'pkr':
    pkr = int(input("Enter Amount in PKR: "))
    pkrtousd(pkr)

elif currency == 'USD' or currency == 'usd':

    usd = int(input("Enter Amount in USD: "))
    usdtopkr(usd)

else:
    print("NOT A VALID COMMAND TERMINATING......")
    sys.exit()

