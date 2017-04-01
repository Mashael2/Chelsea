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

def doors(H1, LD, RD, CL, ML, LI, LO, RI, RO,  GS):
    """
    determine if the doors can open or not
    Args:
        H1, LD, RD, CL, ML, LI, LO, RI, RO, GS
    Returns
        what doors are open or closed.
    """
    #door state
    canOpen = 0
    rOpen = 0
    lOpen = 0

    # gear 0 False 1 True 2 Invalid
    gsPark = 0
    # pattern for checking gear shift
    #pattern = re.compile("r[PpNnDd123Rr]")
    pattern = [ ' P', ' N', ' D', ' 1', ' 2', ' 3', ' R'] 
    # Determine gear shift
    if GS == " P":
        gsPark = 1
        canOpen = 1
    elif  GS.upper() in pattern:  #pattern.match(GS) and len(GS) == 1:
        gsPark = 0
        canOpen = 0
    else :
        gsPark = 2
        canOpen = 0

    if canOpen == 1 and int(ML) == 1:
        #Test if Left door can be opened
        if (int(LI) == 1 and int(CL) == 0) or (int(LO) == 1 or int(LD) == 1):
            lOpen = 1
        else:
            lOpen = 0

        # Test if right door can open
        if (int(RI) == 1 and int(CL) == 0) or int(RO) == 1 or int(RD) == 1:
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
        doorText = doorText + "Both doors stay closed."
    elif lOpen == 1 and rOpen == 1:
        doorText = "Both doors open."
    
    else:
        if lOpen == 1:
            doorText = "Left door opens."
        else:
            doorText = "Right door opens."
    return doorText




#Main Function
def main():
    """
    Test Function
    """



if __name__=="__main__":
    # Call Main
    main()

    exit(0)
