import csv  # to read the csv file

# this class is for reading exchange rates and changing money between CAD and USD
class ExchangeRates:

    def __init__(self, fn):
        # save the file name and start with no rate
        self.fn = fn
        self.r = None

    def getrate(self):
        # open the csv file and read it
        with open(self.fn, "r", encoding="utf-8") as f:
            info = csv.reader(f)
            rows_lst = []
            for l in info:
                rows_lst.append(l)  # put every row into a list

        # find where the USD/CAD column is
        header = rows_lst[0]
        usd_index = header.index("USD/CAD")

        # take the last line (latest rate)
        lastl = rows_lst[-1]

        # get the rate text
        rt_txt = lastl[usd_index].strip()

        # turn the rate into a number
        number_rate = float(rt_txt)

        # save it so we can use it later
        self.r = number_rate

    def convert(self, amount, inputcurr, outputcurr):
        # if we don’t have the rate yet, go get it
        if self.r == None:
            self.getrate()

        r = self.r  # use the rate we got

        # usd to cad
        if inputcurr == "USD" and outputcurr == "CAD":
            return amount * r
        
        # cad to usd
        if inputcurr == "CAD" and outputcurr == "USD":
            return amount / r

        # if something else, i don't know
        print("I don't know that one.")
        return None


# main part
file_name = "BankOfCanadaExchangeRates.csv"

# ask how much
amt_input = input("How much money? ")
amt = float(amt_input)

# ask what currency it’s from
inputcurr = input("From which currency (CAD or USD)? ").upper()

# ask what currency it’s to
outputcurr = input("To which currency (CAD or USD)? ").upper()

# make the object and convert it
ex = ExchangeRates(file_name)
result = ex.convert(amt, inputcurr, outputcurr)

# print it out
if result != None:
    print(str(round(amt, 2)) + " " + inputcurr + " is equal to " + str(round(result, 2)) + " " + outputcurr)

