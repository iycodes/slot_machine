# 3*3 slot machine
import random
import time
# the roughWork file is where i did tested and worked on most of my functions before bringing them here
# from .roughWork import printSlotMachineResult

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3


userData = {
    "balance":20
}
state = {
    "spinState":[],
}

symbolDictionary = {
    "A": 5,
    "B": 4,
    "C": 6,
    "D": 4
}  # converted to an array and used as the symbols in our slot machine


def yesOrNoInput(text):
    res = input(f"{text}: ")
    if(res in ("yes", "y", "YES", "Y")):
        return True
    if(res in ("no" , "n" , "NO" , "N")):
        return False
    yesOrNoInput(text)
# yesOrNoInput("would you like to ")


def deposit():
    ans = input("would you like to deposit before proceeding? \nreply no to cancel, anything else to proceed : ")
    if(ans in ("no" , "n" , "NO" , "N")):
        return
    while True:
        amount = input("How much would you like to deposit ? $")
        # isdigit() this method automatically converts to number before checking
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                userData["balance"] += amount
                break
            else:
                print("please enter an amount greater than zero")
        else:
            print("Please enter a number")
    # userData["balance"] = amount
    print(f'your new balance is ${userData["balance"]}')
    return amount
# deposit()

def getNoOfLinesToBetOn():
    while True:
        lines = input(
            f"Enter no of lines to bet on eg 1, 2.. or all({MAX_LINES}): ")
        if lines.isdigit():
            _lines = int(lines)
            if _lines > MAX_LINES:
                print(f"You can only bet on a max of {MAX_LINES} lines")
            else:
                # print(int(len(lines)), lines)
                break
        else:
            print(f"Please enter valid line number(s)")

    return _lines


# getNoOfLinesToBetOn()

def spinSlotMachine(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    columns = []
    availaibleSymbols = allSymbols[:]
    # "_" in just another term for "i", especially if we dont need the value of i
    for _ in range(cols):
        nestedColumn = []
        for i in range(rows):
            val = random.choice(availaibleSymbols)
            nestedColumn.append(val)
            availaibleSymbols.remove(val)
        columns.append(nestedColumn)
    # print(columns)
    state["spinState"] = columns
    return columns


# spinSlotMachine(ROWS, COLS, symbolDictionary)


def getBet( lines):
    # print(userData["balance"])
    # print(lines)
    while True:
        amount = input(
            f"How much would you like to bet ${MIN_BET}- ${MAX_BET}: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET >= amount:
                print("A bet cannot be less than $1")
            elif MAX_BET <= amount:
                print("You cannot bet more than $100")
            elif amount > userData["balance"]:
                print("Insufficient Funds!")
                res = yesOrNoInput("would you like to deposit?")
                if(res):
                    deposit()
                    if(userData["balance"]>amount):
                        break
                    else:
                        print("Not enough balance for specified amount, retrying...")
                        time.sleep(2)

            else:
                userData["balance"] -= amount
                print("valid")
                break

    return amount


def printSlotMachine(arr):
    # printed the spinned array them in a slot machine like format in the terminal
    duplicatedArr = arr[:]
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            # duplicatedArr[i][j] = arr[j][i] wanted to transpose the array here for more fun but decided to leave it as it..
            # print(f"|{duplicatedArr[i][j]}|", end="")
            print(f"|{arr[i][j]}|", end="")
        print()
    return (arr)

# printSlotMachine(spinSlotMachine(ROWS, COLS, symbolDictionary))

def checkWinnings(n, arr, amt):
    # n is no of lines chosen, arr is the spinned array result, amt is the bet amount
    nl = 0  # nl is no of lines that were equal after spinning
    # n = n[1]
    # n = str(n)
    # print(n)
    
    for row in arr:
        isLineWon = True
        a = row[0]
        for val in row:
            if(a!=val):
                isLineWon=False
        if(isLineWon):
            nl+=1
    print(nl)
    if(nl>0):
        winning = amt * (2**n)
        if(nl>=n):        
            userData["balance"] += winning    
            print(f"you have won ${winning} \nyour balance is {userData['balance']} ")
            
            retry() 
        else:
            userData["balance"] += amt
            print(f"your bet amt has been returned \nyour balance is ${userData['balance']}")
            retry() 
    else:
        # userData["balance"] -= amt
        print(f"you have lost ${amt}, \nyour balance is ${userData['balance']}")
        retry() 



# testingArr = [["A","A","B"],["C","C","F"], ["D","D","D"] ]
# checkWinnings(2,testingArr, 50)

def main1():
    no_lines = getNoOfLinesToBetOn()
    bet = getBet(no_lines)
    print(
        f"You are betting ${bet} on {no_lines} {'line' if bet==1 else 'no_lines'}. ")
    spinnedData = spinSlotMachine(ROWS, COLS, symbolDictionary)
    printSlotMachine(spinnedData)
    checkWinnings(no_lines, spinnedData, bet)

def main(): 
    if(len(state["spinState"])>0):
        printSlotMachine(state["spinState"])   
    deposit()
    no_lines = getNoOfLinesToBetOn()
    bet = getBet(no_lines)
    print(
        f"You are betting ${bet} on {no_lines} {'line' if bet==1 else 'no_lines'}. ")
    spinnedData = spinSlotMachine(ROWS, COLS, symbolDictionary)
    printSlotMachine(spinnedData)
    checkWinnings(no_lines, spinnedData, bet)



def retry():
    ans = yesOrNoInput("would you like to try again")
    if(ans):
        main()
    else:
        return

def factorial(num):
    mul = 1
    for i in range(num):
        mul = mul * (i+1)
    return mul
main()

#used this in the getSpecificLinesToBetOn function to assist in validating the user input
def perm(x, y):
    a = factorial(x)
    b = factorial(x-y)
    res = a/b
    # print(res)
    return res

# this is for betting on or more specific lines, might come back to implement this in the future..
# for now im just getting the number of lines eg 1 or 2 or 3 or all lines..
# this would allow the player to bet on specific line eg line one, line 3, line 2 and 3 , etc..
# obviously with this i would have to raise the reward as the risk is much higher..
def getSpecificLinesToBetOn():
    while True:
        lines = input(
            f"Enter nolines to bet on eg 1 or 1,2 or 1,2,3 between 1- {MAX_LINES}: ")
        _lines = lines.replace(",", "")
        a = perm(MAX_LINES, len(_lines))
        mul = 1
        if _lines.isdigit():
            for digit in _lines:
                mul *= int(digit)
                print(mul)
            if (len(lines) > MAX_LINES) or (mul > a):
                print(
                    f"You can only bet on lines 1-{MAX_LINES} , eg 1 only 1,2 1,3 1,2,3 etc.")
            else:
                print(int(len(_lines)), _lines)
                break
        else:
            print(f"Please enter valid line number(s)")

    return (int(len(_lines)), _lines)

#This is to check winnings if allowed the player to choose specific lines instead of just the number of lines
def checkWinningsForSpecificLines(a, b, c):
    # a is the line or lines chosen, b is the spinned array result, c is the bet amount
    # n = 0  # n is no of wins
    a = a[1]
    a = str(a)
    # print(a)
    checkerArr = []
    # l is the array of line(as) that were equal from the slot machine result
    l = []
    w = []   # w is the final array of line(s) won by the player
    for row in b:
        x = row[0]
        d = 0
        for digit in row:
            if digit == x:
                d += 1
        checkerArr.append(d)
        line = 0
    for i in range(len(checkerArr)):
        line += 1
        if checkerArr[i] == len(row):
            # print(i)
            l.append(line)

    # print(checkerArr)
    # print(l)
    s = ""  # s is the line(s) the person won in string format eg "12"
    # print(a)
    # print(l)
    for digit in a:
        print(digit)
        if int(digit) in l:
            w.append(digit)
            s = s+str(digit)

    if a == s:
        # win for staking on a line is 2x , for 2 lines is 4* etc, but no compensation if you win choose 2 lines and win only one, or 3 and win only 1 or 2
        print(f"You won {c * len(s) * 2}")
    else:
        li = ""
        for digit in w:
            li = li+digit+","

        print(f"You lost but got {'lines' if len(w)>1 else 'line'} {li}.")
        retry = input("DO you want tp try again? types in yes or no")
        if (retry == "yes or y"):
            main()
        else:
            return
    # print(s)


