#!/usr/bin/env python3

from colorama import Fore, Back, Style
from myfunctions import isPerfect

maximum_number=500


def main():
      print('Starting to compute prime numbers up to'+str(maximum_number))
      for i in range(1,maximum_number):
            if isPerfect(i):
                  print ('Number '+str(i)+' is perfect.')

                  



if __name__ == "__main__":
        main()