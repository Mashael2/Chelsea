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




def data():
    data = []
    with open('test.csv') as data_file:
        data = data_file.read()
        print(data)

    rows = data.split('R1')
    for i in rows:
        print(i)

    code = rows[0].split(',')
    for i in code:
        print(i)







#Main Function
def main():
    """
    Test Function
    """
    data()


if __name__=="__main__":
    # Call Main
    main()

    exit(0)
