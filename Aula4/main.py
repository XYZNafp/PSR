#!/usr/bin/env python3


# Imports

import argparse # Defines arguments required to run the program
import pprint # Allows for prettier printings of dictionaries
import readchar # To read input characters from keyboard
import time # To register the passage of time
import random
from collections import namedtuple #
import colorama # Expands customization options for text
from colorama import Fore, Back, Style # Allows customization of font color, background color and characters opacity
colorama.init(autoreset=True) # Resets colorama styling at the start of every print


# Global Variables

input_tuple=namedtuple('input_tuple', ['q','a','t']) # Question, Answer and Time


# Functions

# The character recognition is returned as ASCII code


def CountMode(threshold):  # Mode where the test ends after 'threshold' inputs
    print('The test will end after ' + str(threshold)+ 'inputs.')
    print('Pressing any key will begin the test.\n')

    # Starts a countdown after pressing a key
    for i in range(1,4): 
        print ('The test will begin in '+ str(4-i)+ ' seconds.\n')
        time.sleep(1)

    inputs=[]

    time_b4_exec=time.time()
    test_interrupt = False
    

    
    for i in range(1,threshold+1): # Defines a range
        target_input=chr(random.randint(97,122))
        time_b4=time.time()
        print("Type "+ target_input)
        typed_input= readchar.readchar()

        if typed_input == chr(27):   # Clicking the ESC button
            time_after = time.time() # Stops time function
            test_interrupt= True    # And interrupts function
            break

        time_after = time.time()
        if typed_input == target_input:
            print ('Correct! You typed '+ typed_input, '\n')
        else:
            print('Incorrect! It was '+ target_input, ' but you typed '+typed_input, '\n')

        duration=time_after-time_b4

        input=input_tuple(q=target_input,a=typed_input,t=duration)

        inputs.append(input)

    if not test_interrupt:
        print('\nThe test has now been completed!\n')
    else:
        print('\nThe test has been interrupted.\n')

    return inputs, time_b4  





        


def buildDict(inputs, abs_b4_time):  # inputs = list of namedTuples
    dict_keys = ['accuracy','types','n_hits','n_types','test_duration','test_end','test_start','type_avg_dur','hit_avg_dur','miss_avg_dur']
    stat_dict = dict.fromkeys(dict_keys,0) # keys = list , values = 0
    #! Any namedTuple can be accessed either by x[1] or x.argument
    total_hit_time = 0
    total_miss_time = 0
    n_misses = 0
    
    for i in range(0,len(inputs)): #len() returns nº of elements of the list, which index starts at 0
        #//current_tuple = inputs[i]
        #* Number of hits
        if inputs[i].a == inputs[i].q:
            stat_dict['n_hits'] += 1
            #* Total hit time, yet to be divided by the number of hits
            total_hit_time += inputs[i].t
        else:
            total_miss_time += inputs[i].t
            #Number of misses - *only used in mid calculations*
            n_misses += 1
 
        #* Test duration
        stat_dict['test_duration'] += inputs[i].t



    # Number of types
    stat_dict['n_types'] = len(inputs)

    # Accuracy
    if stat_dict['n_types'] == 0 :
        stat_dict['accuracy'] = 0
    else:
        stat_dict['accuracy'] = stat_dict['n_hits'] / stat_dict['n_types']

    # Test start
    stat_dict['test_start'] = time.ctime(abs_b4_time)

    # Test end
    stat_dict['test_end'] = time.ctime(abs_b4_time + stat_dict['test_duration'])

    # Average type time 
    # The test time won't ever be 0 seconds, so there ain't a problem by dividing by the time
    if len(inputs) == 0:
        avg_type_time = 0
    else:
        avg_type_time = stat_dict['test_duration'] / len(inputs) #!Trick to assure only 3 decimal points
    
    stat_dict['type_avg_dur'] = avg_type_time

    # Average miss time
    if n_misses == 0:
        miss_avg_time = 0
    else:
        miss_avg_time = total_miss_time / n_misses  

    #// stat_dict['miss_avg_dur'] = str(miss_avg_time) + 's'
    stat_dict['miss_avg_dur'] = miss_avg_time

    # Average hit time
    if stat_dict['n_hits'] == 0:
        hit_avg_time =0
    else:
        hit_avg_time = total_hit_time / stat_dict['n_hits']
    
    #//stat_dict['hit_avg_dur'] = str(hit_avg_time) + 's'
    stat_dict['hit_avg_dur'] = hit_avg_time

    # Types
    stat_dict['types'] = inputs
    return stat_dict




def main():
    
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy') 
    parser.add_argument('-utm','--use_time_mode', action='store_true',default = False ,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv','--max_value',type=int,required=True,help='Number of seconds/letters of the test') 
    parser.add_argument('--uw','--use_words',default=False, help='Use word typing mode instead of single character typing (turned off by default)')
    args = parser.parse_args()

    inputs = [] #* This will be the list of namedTuples that the function buildDict will use to build the statistics dictionary
    my_dict = {}


    #//time_b4_exec = time.time() # In order to build the dictionary the buildDict should receive a absolute time as well.
    # The line above would be wrong because it wouldn't take into consideration the time for the user to start nor the countdown

    if args.use_time_mode == True:
        inputs ,time_b4_exec = modoTimed(args.max_value)
    else:
        inputs ,time_b4_exec = CountMode(args.max_value)
        
    #At this point in the programm there should already be the list of namedTuples on which the buildDict function will work with
    my_dict = buildDict(inputs,time_b4_exec)
    print(Fore.GREEN + 'Your test statistics are:','\n')
    pprint.pprint(my_dict,sort_dicts=False)





if __name__ == "__main__":
    main()
