def isNumber(userInput):
    try:
        userInput=float(userInput)
        print("Number has been input")
        return True
    except ValueError:
        print("String has been input")
        return False

userInput=input("Enter number which has to be converted: ")
if isNumber(userInput)==False:
    print("Please enter numbers only")
else:
    userInput=float(userInput)
    convertedNum=userInput*0.011
    print(userInput,"INR in USD is ",round(convertedNum,2))
