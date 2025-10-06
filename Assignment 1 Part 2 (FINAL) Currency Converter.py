import csv # Importing the data in CSV file

# This class is for reading exchange rates and converting between CAD and USD
class ExchangeRates:

    def __init__(self, fn):
        self.fn = fn
        self.r = None

    def getrate(self):
        # Open the exchange rate file and read data
        with open(self.fn, "r", encoding="utf-8") as f:
            info = csv.reader(f)
            rows_lst = []
            for l in info:
                rows_lst.append(l) # Collect each row from the file then turn into a list

        # Count how many rows there are
        count = 0
        for item in rows_lst:
            count = count + 1

        # Get the most recent exchange rate (Last row)
        lastl = rows_lst[count - 1]

        # Grab the rate as a string
        rt_txt = lastl[1]


        # Turn the string into individual characters then bring them back together
        letters = []
        for ch in rt_txt:
            letters.append(ch)

        joined = ""
        for x in letters:
            joined = joined + x


        # Convert the combined string into a number
        number_rate = float(joined)

        # Save rate for later use
        self.r = number_rate

    def convert(self, amount, inputcurr, outputcurr):
        # If we don't already have the rate, go get it
        if self.r == None:
            self.getrate()

        r = self.r # Use the stored exchange rate


        # If converting from USD to CAD
        if inputcurr == "USD":
            if outputcurr == "CAD":
                a1 = amount * r
                return a1
            
        # If converting from CAD to USD
        if inputcurr == "CAD":
            if outputcurr == "USD":
                a2 = amount / r
                return a2

        # If the currencies aren't recognized, show a message
        print("I don't know")
        return None

# Ask the user for the input values
file_name = "BankOfCanadaExchangeRates.csv"

amt_input = input("How much money? ")
amt = float(amt_input) # Turn the user input into a number

# Ask for source currency and convert it into uppercase
inputcurr = input("From which currency (CAD or USD)? ")
inputcurr = inputcurr.upper()

# Ask for target currency and convert it into uppercase
outputcurr = input("To which currency (CAD or USD)? ")
outputcurr = outputcurr.upper()

# Create an exchangerates object and do the conversion
ex = ExchangeRates(file_name)
result = ex.convert(amt, inputcurr, outputcurr)

#If conversion works, show result
if result != None:
    print(str(round(amt, 2)) + " " + inputcurr + " is equal to " + str(round(result, 2)) + " " + outputcurr)

        