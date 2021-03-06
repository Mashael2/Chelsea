#!/usr/bin/env python3
import sys


def printDigit(d):
    """
    A function to print the digits
    """
    try:
        i = int(d)
    except:
        print("Error: Zip code is not all numeric")
        return""
    if(i == 1):
        return(":::||")
    if(i == 2):
        return("::|:|")
    if(i == 3):
        return("::||:")
    if(i == 4):
        return(":|::|")
    if(i == 5):
        return(":|:|:")
    if(i == 6):
        return(":||::")
    if(i == 7):
        return("|:::|")
    if(i == 8):
        return("|::|:")
    if(i == 9):
        return("|:|::")
    if(i == 0):
        return("||:::")
        #return""

def printBarCode(zipCode):
    """
    A function to print the bar code
    """
    zipSum = 0
    checkDigit = 0

    for i in zipCode:
        zipSum += int(i)

    while ((zipSum%10) != 0):
        checkDigit += 1
        zipSum += 1

    #printDigit(checkDigit)
    
    if len(zipCode) != 5:
        print("Error: Zip code is not 5 digits")
        return""

    barcode = "|"
    barcode += printDigit(zipCode[0]) 
    barcode += printDigit(zipCode[1]) 
    barcode += printDigit(zipCode[2]) 
    barcode += printDigit(zipCode[3]) 
    barcode += printDigit(zipCode[4])
    barcode += printDigit(checkDigit)
    barcode += "|" 
    return barcode

        
# Main function
def main():
    """
    Test Function
    """
    userInput = input("Enter Zip code: ")
    printBarCode(userInput)


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
