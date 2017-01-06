def main():
    creditNumber = ""
    validNumber = []
    totalNumber = 0
    creditNumber = raw_input("Please enter a credit card number to validate: ") 
    creditNumber = creditNumber[:len(creditNumber)-1]
    creditNumber = creditNumber[::-1]
    for counter in creditNumber:
            validNumber.append(int(counter))
    for counter in range(0, len(validNumber) , 2):
            validNumber[counter] *= 2
            if(validNumber[counter] > 9):
                validNumber[counter] -= 9
    for counter in range(len(validNumber)):
        totalNumber += validNumber[counter]
    print totalNumber
    totalNumber %= 10
    print totalNumber
    return
if __name__ == "__main__":
    main()
