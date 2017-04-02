#!/usr/bin/env python3
import sys
from Chelsea_task2_hw7 import printBarCode
from urllib.request import urlopen


def testBarCode():
    """
    Testing BarCode
    """
    test = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt")
    test = test.read().decode()
    test = test.splitlines()
    for testCode in test:
        print("Enter zip code: ",testCode)
        print(printBarCode(testCode))


# Main function
def main():
    """
    Test Function
    """
    testBarCode()
    return


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
