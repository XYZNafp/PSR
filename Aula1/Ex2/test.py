#!/usr/bin/env python3

from colorama import Fore, Back, Style

maximum_number=10

def isPrime(value):
      
      for i in range(2,value):
            if value%i == 0:
                #print('the number ' + str(value) + ' is not prime because we can divide by ' + str(i))
                return False
      return True

def main():
      print('Starting to compute prime numbers up to'+str(maximum_number))
      for i in range(0,maximum_number):
            if isPrime(i):
                    print('Number ' + Fore.BLUE+ Back.LIGHTGREEN_EX+ str(i)+  Style.RESET_ALL + " is prime.")
            else:
                    print('Number ' +Back.LIGHTRED_EX+Fore.YELLOW+ str(i) + Style.RESET_ALL+ ' is not prime.')




if __name__ == "__main__":
        main()