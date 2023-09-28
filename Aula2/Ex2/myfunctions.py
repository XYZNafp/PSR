#!/usr/bin/env python3

def getDividers(value):
      
      dividers = []
      for i in range(1,value):
            if value%i == 0:
                dividers.append(i)
      return dividers

def isPerfect(value):
       dividers=getDividers(value)

       return value == sum(dividers)
