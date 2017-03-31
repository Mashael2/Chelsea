#!/usr/bin/env python3
import sys



def printDigit(d):
    """
    A function to print the digits
    """
    value = {
            0: "||:::",
            1: ":::||",
            2: "::|:|",
            3: "::||:",
            4: ":|::|",
            5: ":|:|:",
            6: ":||::",
            7: "|:::|",
            8: "|::|:",
            9: "|:|::",
            }
    return value.get(d, "Zip code is not all numeric")



def printBarCode(zipCode):
    """
    A function to print the bar code
    """

    barcode = ["|",]
    digits = [int(i) for i in str(zipCode)]

    for d in digits:
        barcode.append(printDigit(d))

    CheckDigit = sum(digits) % 10
    if checkDigit % 10 != 5:
        print("Zip code is not 5 digits")
    else:
        checkDigit = printDigit(checkDigit)
        



# Main function
def main():
    """
    Test Function
    """
    userInput = input("Enter a zipcode: ")
    printBarCode(userInput)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
