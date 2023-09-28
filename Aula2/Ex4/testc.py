#!/usr/bin/env python3

import argparse

import readchar

from colorama import Fore, Back, Style
from myfunctions import isPerfect

maximum_number=500

def countNumbersUpTo(stop_char):
       
       print ('Start typing')

       keys =[]
       while True:
          key = readchar.readkey()
          keys.append(key)
          print('You typed '+key)

          if key == stop_char:
                break
     
       print(keys)

       n_numeric = 0
       for key in keys:
          if key.isnumeric():
               n_numeric +=1

          print('Your pressed on '+str(n_numeric)+' numeric keys')




def main():
      
     countNumbersUpTo('x')



if __name__ == "__main__":
        main()