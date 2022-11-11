import random

MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 100

ROWS = 3
COLS = 3

symbolCount = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

symbolValue = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
}


def checkWinnings (columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range (lines):  ## Looping through every row that the user bet on.
        symbol = columns [0] [line]  ## The Symbol that I want to check is in the first columns of the current row.
        for column in columns:  ## Loops through every single column
            symbolToCheck = columns [line]  ## symbol to check is equal to the column at the current row.
            if symbol != symbolToCheck:  ## Checks if the symbols are not the same.
                break
        else:  ## If all the symbols were the same, then the user won.
            winnings += values [symbol] * bet
            winningLines.append (lines + 1)
    return winnings, winningLines


def getSlotMachineSpin (rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items ():
        for _ in range (symbolCount):
            allSymbols.append (symbol)

    columns = []
    for _ in range (cols):
        column = []
        currentSymbols = allSymbols [:]
        for _ in range (rows):
            value = random.choice (currentSymbols)
            currentSymbols.remove (value)
            column.append (value)

        columns.append (column)
    return columns


def printSlotMachine (colunms):  ## --- Transposing
    for row in range (len (colunms [0])):  ## Loops through the columns
        for i, colunm in enumerate (colunms):  ## Looping through every individual column
            if i != len (colunms) - 1:
                print (colunm [row], end = " | ")
            else:
                print (colunm [row], end = "")
        print ()


def deposit ():
    while True:
        amount = input ("Enter how much you want to deposit: $")
        if amount.isdigit ():
            amount = int (amount)
            if amount > 0:
                break
            else:
                print ("Amount must be great then 0.")
        else:
            print ('Not a Valid Number. Please enter a Number.')
    return amount


def getNumberOfLines ():
    while True:
        lines = input (f"Enter the number of line you want the bet on (1-{MAX_LINES})? ")
        if lines.isdigit ():
            lines = int (lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Enter a valid number of lines.")
        else:
            print ('Not a Valid Number. Please enter a Number.')
    return lines


def getBet ():
    while True:
        amount = input ("Enter how much you want to bet on each line: $")
        if amount.isdigit ():
            amount = int (amount)
            if MIN_BET <= amount <= MAX_BET:

                break
            else:
                print (f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print ('Not a Valid Number. Please enter a Number.')
    return amount

def spin(balance):
    lines = getNumberOfLines ()
    while True:
        bet = getBet ()
        totalBet = bet * lines
        if totalBet > balance:
            print (f" You don't have enough to bet that. you current balance is ${balance}")
        else:
            break

    print (f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")

    slots = getSlotMachineSpin (ROWS, COLS, symbolCount)
    printSlotMachine (slots)
    winnings, winningLines = checkWinnings (slots, lines, bet, symbolValue)
    print (f"You Won ${winnings}.")
    print (f"You won on", *winningLines)

    return winnings - totalBet
def main ():
    balance = deposit ()
    while True:
        print(f"Current Balance is ${balance}")
        anwser = input("Press enter to play (q to quit).")
        if anwser == 'q':
            break
        balance += spin(balance)

    print(f" You left with ${balance}")

main()
