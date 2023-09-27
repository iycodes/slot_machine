
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

arr = [[3, 1, 0], [2, 4, 6], [5, 8, 9]]

# [[3, 2, 5], [1, 4, 8], [0, 6, 9]]
newArr = []
l = len(arr)

for row in arr:
    for digit in row:
        # print(digit)
        newArr.append(digit)
ano = []
for i in range(l):
    ano.append([])
for item in newArr:
    ind = newArr.index(item) % l
    # print(ind)
    for i in range(l):
        if ind == i:
            ano[i].append(item)

reArr = []
for item in newArr:
    for i in range(l):
        if i == newArr.index(item) % l:
            reArr.append(item)


def printSlotMachineResult(arr):
    duplicatedArr = arr[:]
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            duplicatedArr[i][j] = arr[j][i]
            print(f"|{duplicatedArr[i][j]}|", end="")
        print()
    # print(duplicatedArr)


symbolDictionary = {
    "A": 3,
    "B": 4,
    "C": 3,
    "D": 2
}  # converted to an array and used as the symbols in our slot machine


def allSymbols(dictionary):
    symbolsArr = []
    for item, count in dictionary.items():
        # print(item, count)
        for _ in range(count):
            symbolsArr.append(item)
    print(symbolsArr)


# allSymbols(symbolDictionary)

def factorial(num):
    mul = 1
    for i in range(num):
        mul = mul * (i+1)
    return mul


def perm(x, y):
    a = factorial(x)
    b = factorial(x-y)
    res = a/b
    print(res)
    return res


def checkWinnings(a, b, c):
    # a is the line or lines chosen, b is the spinned array result, c is the bet amount
    n = 0  # n is no of wins
    a = str(a)
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

        print(f"You lost but got {'lines' if len(w)>1 else 'line'} {li}")
    print(s)


tstArr = [[2, 0, 2], [3, 3, 3], [5, 5, 5]]
# checkWinnings(12, tstArr, 50)


def getLinesToBetOn():
    while True:
        lines = input(
            f"Enter lines to bet on eg 1 or 1,2 or 1,2,3 between 1- {MAX_LINES}: ")
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


getLinesToBetOn()
