# Ask user for interest rate then store it in a float
a = input("What is the interest rate (0.055 is 5.5%)")
x = float(a)

# Ask for amount of years the mortgage will last then convert into integer
b = input("Years: ")
y = int(b)

# Ask for the principal then store into a float
c = input("Principal: ")
z = float(c)

# This class is used to calculate the different types of Mortgage payments
class MortgagePayment: 
    # Save the rate and the years to use later
    def __init__(self, rate, years):
        self.rate = rate
        self.years = years

    # Main function to calculate payments    
    def do_pmt(self, p):
        # Take the yearly rate, turn it into semi‑annual, then make it the effective annual rate
        semiannualrate = self.rate/2
        growth = (1 + semiannualrate) ** 2
        annualeffective = growth - 1 
        
        # Convert annual effective rate to different compounding periods
        rmnth = (1+ annualeffective) ** (1 / 12) - 1
        rs_mnth = (1 + annualeffective) ** (1/24) - 1
        r_bwkly = (1 + annualeffective) ** (1/26) - 1
        rwkly = (1 + annualeffective) ** (1/52) - 1
        
         # Calculate the number of payments for each frequency
        nmnth = self.years * 12
        ns_mnth = self.years * 24
        nbiwkly = self.years * 26
        nwkly= self.years * 52 
        
        # Formula used to break down loan repayment over time
        def calcpmt(r , n):
            x = (r * p)
            y = (1 - (1 + r) ** -n)
            return (x / y)
        
         # Calculate regular payments for each frequency 
        month = calcpmt(rmnth, nmnth)
        semi_mnth = calcpmt(rs_mnth, ns_mnth)
        bi_wkly = calcpmt(r_bwkly, nbiwkly)
        wkly = calcpmt(rwkly, nwkly)

        # Rapid payments made more often by dividing the monthly amount in half or quarters    
        acceleratebiweekly = month / 2
        accelerateweekly = month / 4
        
        # Return all rounded to 2 decimals
        return (round(month, 2), 
            round(semi_mnth, 2), 
            round(bi_wkly, 2), 
            round(wkly, 2), 
            round(acceleratebiweekly, 2), 
            round(accelerateweekly, 2))

# Creating the mortgagepayment object with inputting years and the rate
mortgage = MortgagePayment(x, y)
payment_tuple = mortgage.do_pmt(z)

# Labelling each payment type and then the result
labels = ["Monthly", "Semi-monthly", "Bi-weekly", "Weekly", "Rapid Bi-weekly", "Rapid Weekly"]
for label, payment in zip(labels, payment_tuple):
    print(f"{label} payment: ${payment}")

