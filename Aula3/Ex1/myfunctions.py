#!/usr/bin/env python3

def getDividers(value):
      
      dividers = []
      limit=round(value/2)+1
      for i in range(1,limit):
            if value%i == 0:
                dividers.append(i)
      return dividers

def isPerfect(value):
       dividers=getDividers(value)

       return value == sum(dividers)
