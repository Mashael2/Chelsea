#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 student1 <student1@CS3030_87>
#


#===========================================================================
#
#       File: Chelsea_task1_module1_hw7.py 
#
#       Usage: ./Chelsea_task1_module1_hw7.py
#
#   Description:
#
#       Options: ---
#       ReqOPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#  ORGANIZATION:
#       CREATED: 03/03/2017 14:27
#      REVISION:  ---
#===========================================================================

import sys
import re

def doors(H1, LD, RD, CL, ML, LI, LO, RI, GS):
    """
    
    """

    #door state
    canOpen = 0
    rOpen = 0
    lOpen = 0

    # gear 0 False 1 True 2 Invalid
    gsPark = 0
    # pattern for checking gear shift
    pattern = re.compile("/[PpNnDd123Rr]/g")

    # Determine gear shift
    if GS == "p" or GS == "P":
        gsPark = 1
        canOpen = 1
    elif pattern.match(GS) and len(GS) == 1:
        gsPark = 0
        canOpen = 0
    else :
        gsPark = 2
        canOpen = 0

    if canOpen == 1 and ML == 1:
        #Test if Left door can be opened
        if (LI == 1 and CL == 0) or (LO == 1) or LD == 1:
            lOpen = 1
        else:
            lOpen = 0

        # Test if right door can open
        if (RI == 1 and CL == 0) or (RO == 1) or (RD == 1):
            rOpen = 1
        else:
            rOpen = 0
    else:
        lOpen = 0
        rOpen = 0

    doorText = ""
    if canOpen == 0 or (lOpen == 0 and rOpen == 0):
        if gsPark == 2:
            doorText = "Invalid Record: "







#Main Function
def main():
    """
    Test Function
    """



if __name__=="__main__":
    # Call Main
    main()

    exit(0)
