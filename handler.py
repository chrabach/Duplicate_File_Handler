# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 11:33:59 2021

@author: Christopher
"""

import sys
import os

args = sys.argv

#sys.argv = [argv[0], "../Duplicate_File_Handler"]




if len(args) != 2:
    print("Directory is not specified")

else:
    directory = args[1]





    for root, dirs, files in os.walk(directory, topdown = False):
       for name in files:
          print(os.path.join(root, name))
       #for name in dirs:
       #   print(os.path.join(root, name))
