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

#5b

       numerical_keys=[]
       for key in keys:
           if key.isnumeric():
            numerical_keys.append(key)

            print('Numerical keys ' +str(numerical_keys))

#5c
d_keys={}
i=0
for key_idx, key in enumerate(keys):
     d_keys[key_idx]=key
print('d_keys = '+str(d_keys))

#5d

numerical_keys.sort()
print('Numerical keys '+str(numerical_keys))

#5e

numerical_keys2=[x for x in keys if x.isnumeric()]

d_keys2={idx:x for idx,x in enumerate(keys)}


def main():
      
     countNumbersUpTo('x')



if __name__ == "__main__":
        main()