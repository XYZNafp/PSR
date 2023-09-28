#!/usr/bin/env python3

import argparse

import readchar

from colorama import Fore, Back, Style
from myfunctions import isPerfect

maximum_number=500

def printAllCHarsUpTo():
       #Ler carater no terminal
       print('Press a key to read a char')
       key=readchar.readkey()
       print('User pressed '+key)

       #Calcular número associado ao carater
       number=ord(key)
       print('Corresponding number is '+str(number))

       #percorrer números desde o espaço (32) até ao n lido
       # e imprimir o número desejado em cada interação 

       chars_to_print=[]
       for i in range(32, number):
              chars_to_print.append(chr(i))

              print(''.join(chars_to_print))



def main():
      
     printAllCHarsUpTo()



if __name__ == "__main__":
        main()