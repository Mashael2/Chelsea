#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 student1 <student1@CS3030_87>
#


#===========================================================================
#
#       File: Chelsea_task1_hw7.py 
#
#       Usage: ./Chelsea_task1_hw7.py
#
#   Description:
#
#       Options: ---
#       ReqOPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#        AUTHOR: 
#  ORGANIZATION:
#       CREATED: 03/03/2017 14:27
#      REVISION:  ---
#===========================================================================

import sys
import csv
import Chelsea_task1_module1_hw7 as module1
from urllib.request import urlopen

def test():
    data = []
    with open('test.csv') as data_file:
        data = data_file.read()
        print('raw', data)
    
    rows = data.split('R1')
    for i in rows:
        print('first split', i)

    code = rows[1].split(',')
    for i in code:
        print('second split', i)

#---------------------
    
url = 'http.icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv'


def data():
    """
    open file and show locked doors
    """

    f = open('test.csv')
    csv_f = csv.reader(f)
    print(csv_f)


    for row in csv_f:
        print("Reading Record", row[0], ' : ')
        print("Left dashboard switch (0 or 1): ", row[1])
        print("Right dashboard switch (0 or 1): ", row[2])
        print("Child lock switch (0 or 1): ", row[3])
        print("Master unlock switch (0 or 1): ", row[4])
        print("Left inside handle (0 or 1): ", row[5])
        print("Left outside handle (0 or 1): ", row[6])
        print("Right inside handle (0 or 1): ", row[7])
        print("Right outside handle (0 or 1): ", row[8])
        print("Gear shift position (P,N,D,1,2,3,or R):", row[9])


        print(module1.doors(row[1], row[2], row[3], row[4], row[5],
            row[6], row[7], row[8], row[9]))

#Main Function
def main():
    """
    Test Function
    """
    #test()
    data()

if __name__=="__main__":
    # Call Main
    main()

    exit(0)
