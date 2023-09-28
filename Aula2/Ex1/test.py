#!/usr/bin/env python3

from colorama import Fore, Back, Style

maximum_number=500

def getDividers(value):
      
      dividers = []
      for i in range(1,value):
            if value%i == 0:
                dividers.append(i)
      return dividers

def isPerfect(value):
       dividers=getDividers(value)

       return value == sum(dividers)

def main():
      print('Starting to compute prime numbers up to'+str(maximum_number))
      for i in range(1,maximum_number):
            if isPerfect(i):
                  print ('Number '+str(i)+' is perfect.')

                  



if __name__ == "__main__":
        main()