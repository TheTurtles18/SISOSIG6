"""CSC 161 Project: Algorithmic Trading

Alex Crowley
Lab Section TR 12:30-1:45pm
Fall 2017
"""
def bookkeep(order,price,stock,Balance):
        if order == "buy":
            amount = float(Balance//price)
            stock = float(stock + amount)
            Balance = float(Balance - (amount*price))
            return stock, Balance
        elif order == "sell":
            Balance = float(Balance)
            stock = float(stock)
            price = float(price)
            Balance = (Balance + (stock*price))
            stock = 0
            return stock, Balance

def get_adj_close1(line):
    date, open_, high, low, close, volume, adj_close = line.split(",")
    return adj_close

def get_adj_close2(line):
    date, open_, high, low, close, volume, adj_close = line.split()
    return adj_close

def alg_mine(filename):
# I am importing stock data for the S&P 500, a major index fund, and comparing
# the daily percentage changes in its price to that of an Apple/Microsoft stock.
# If the percentage change is .5% higher than that of the S&P 500 index for that
# day, the program will sell, and if the percentage change is .5% lower than that
# of the S&P 500 then the program will buy.

# First, the program will open and read in the price information for the S&P 500
        SP_500 = open("GSPC.txt", "r")
        in_lines = SP_500.readlines()
               
        file = open(filename, "r")
        lines = file.readlines()
        new_lines = lines[::-1]
        day = 0

        # Variable for Apple holdings
        AAPL = 0.0
        # Variable for Microsoft holdings
        MSFT = 0.0
        # Variable for account balance
        Balance = 1000.0
        #Variable for quantity of stocks purchased/sold (as many as possible)
        amount = 0.0

        line_A = new_lines[day]
        line_SP = in_lines[day+1]
        price_A = eval(get_adj_close1(line_A))
        yesterday_price_A = price_A
        price_SP = eval(get_adj_close2(line_SP))
        yesterday_price_SP = price_SP
        day += 1
        if filename == "AAPL.csv":
                while day < len(new_lines)-2:
                        line_A = new_lines[day]
                        line_SP = in_lines[day+1]
                        price_A = eval(get_adj_close1(line_A))
                        price_SP = eval(get_adj_close2(line_SP))
                        change_A = price_A/yesterday_price_A
                        change_SP = price_SP/yesterday_price_SP
                        #If daily change in stock deviates more than .5% from daily
                        # change in stock, will exact an order
                        if change_A < change_SP - .15: 
                                AAPL, Balance = bookkeep("buy",price_A,AAPL,Balance)
                        elif change_A > change_SP + .15 and AAPL != 0:
                                AAPL, Balance = bookkeep("sell",price_A,AAPL,Balance)
                        yesterday_price_A = price_A
                        yesterday_price_SP = price_SP
                        day +=1
                line_A = new_lines[day]
                price_A = get_adj_close1(line_A)
                AAPL, Balance = bookkeep("sell",price_A,AAPL,Balance)
                return AAPL, Balance
        elif filename == "MSFT.csv":
                while day < len(new_lines)-2:
                        line_A = new_lines[day]
                        line_SP = in_lines[day+1]
                        price_A = eval(get_adj_close1(line_A))
                        price_SP = eval(get_adj_close2(line_SP))
                        change_A = price_A/yesterday_price_A
                        change_SP = price_SP/yesterday_price_SP
                        #If daily change in stock deviates more than .5% from daily
                        # change in stock, will exact an order
                        if change_A < change_SP - .15: 
                                MSFT, Balance = bookkeep("buy",price_A,MSFT,Balance)
                        elif change_A > change_SP + .15 and MSFT != 0:
                                MSFT, Balance = bookkeep("sell",price_A,MSFT,Balance)
                        yesterday_price_A = price_A
                        yesterday_price_SP = price_SP
                        day +=1
                line_A = new_lines[day]
                price_A = get_adj_close1(line_A)
                MSFT, Balance = bookkeep("sell",price_A,MSFT,Balance)
                return MSFT, Balance

    
def main():

    filename = input("Enter a filename for stock data (CSV format): ")

    alg1_stocks, alg1_balance = alg_mine(filename)
    
    print("The results are ${0:0.2f} in your balance".format(alg1_balance))
 
if __name__ == '__main__':
    main()

        


    
    
        

    
