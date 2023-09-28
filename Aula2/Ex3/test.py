#!/usr/bin/env python3

import argparse

from colorama import Fore, Back, Style
from myfunctions import isPerfect

maximum_number=500


def main():
      
      parser=argparse.ArgumentParser(description='Script to compute perfect numbers.')
      parser.add_argument('-mn', '--maximum_number', type=int, help='max number.', required=True)
      parser.add_argument('-n', '--name', type=str, help='A name to print.', required=False, default='Toni')
      parser.add_argument('-sl', '--say_hello', help='Say hello?', action='store_true')

      args=vars(parser.parse_args())
      print(args)

      if args['say_hello']:
             print("Hi "+args['name']+' !!!')
             
      
      
      print('Starting to compute prime numbers up to'+str(maximum_number))
      for i in range(1,maximum_number):
            if isPerfect(i):
                  print ('Number '+str(i)+' is perfect.')

                  



if __name__ == "__main__":
        main()