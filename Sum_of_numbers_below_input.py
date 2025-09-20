def main():
    userInput=input("Enter a number: ")
    if not userInput.isdigit():
        print("Enter whole digits only")
        return
    userInput=int(userInput)
    count=0
    sumOfNumbers=0
    while count<userInput:
        count+=1
        sumOfNumbers=sumOfNumbers+count
    print(sumOfNumbers)
if __name__=="__main__":
    main()