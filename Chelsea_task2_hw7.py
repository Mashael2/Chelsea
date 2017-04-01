#!/usr/bin/env python3
import sys



def printDigit(d):
    """
    A function to print the digits
    """
    try:
        d = int(d)
    except:
        print("Error: Zip code is not all numeric")
        return""
    if d == 1:
        return(":::||")
    if d == 2:
        return("::|:|")
    if d == 3:
        return("::||:")
    if d == 4:
        return(":|::|")
    if d == 5:
        return(":|:|:")
    if d == 6:
        return(":||::")
    if d == 7:
        return("|:::|")
    if d == 8:
        return("|::|:")
    if d == 9:
        return("|:|::")
    if d == 0:
        return("||:::")
    return""



def printBarCode(zipCode):
    """
    A function to print the bar code
    """
    
    zipcode = int(zipCode)
    zipcode = str(zipCode)

    if len(zipCode) != 5:
        print("Error: Zip code is not 5 digits")
        return""

    checkDigit = int(zipCode)
    checkD = checkDigit  %10


    barcode = "|"
    barcode += printDigit(zipcode[0])
    barcode += printDigit(zipcode[1])
    barcode += printDigit(zipcode[2])
    barcode += printDigit(zipcode[3])
    barcode += printDigit(zipcode[4])
    barcode += printDigit(checkD)
    barcode += "|"

    return barcode

        

# Main function
def main():
    """
    Test Function
    """
    printBarCode(zipCode)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
