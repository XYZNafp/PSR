#!/usr/bin/env python3

import argparse
import time
import random
from collections import namedtuple
import colorama
from colorama import Fore

colorama.init(autoreset=True)

input_tuple = namedtuple('input_tuple', ['q', 'a', 't'])

def TypeTest(threshold, TimedMode, WordMode):
    print('The test will end after ' + str(threshold) + ' inputs.')
    print('Press any key to begin the test.\n')
    _ = input()

    for i in range(1, 4):
        print('The test will begin in ' + str(4 - i) + ' seconds.\n')
        time.sleep(1)

    inputs = []

    time_b4_exec = time.time()
    test_interrupt = False

    target_input = ""
    if not WordMode:
        target_input = ''.join([chr(random.randint(97, 122)) for _ in range(threshold)])

    for i in range(len(target_input)):
        if TimedMode and time.time() - time_b4_exec > threshold:
            test_interrupt = True
            break

        typed_input = input("Type " + target_input[i] + ": ")

        if typed_input == chr(27):
            test_interrupt = True
            break

        if typed_input == target_input[i]:
            print('Correct! You typed ' + typed_input, '\n')
        else:
            print('Incorrect! It was ' + target_input[i], ' but you typed ' + typed_input, '\n')

        duration = time.time() - time_b4_exec

        input_data = input_tuple(q=target_input[i], a=typed_input, t=duration)
        inputs.append(input_data)

    if not test_interrupt:
        print('\nThe test has now been completed!\n')
    else:
        print('\nThe test has been interrupted.\n')

    return inputs, time_b4_exec

def buildDict(inputs, abs_b4_time):
    dict_keys = ['accuracy', 'types', 'n_hits', 'n_types', 'test_duration', 'test_end', 'test_start', 'type_avg_dur', 'hit_avg_dur', 'miss_avg_dur']
    stat_dict = dict.fromkeys(dict_keys, 0)
    total_hit_time = 0
    total_miss_time = 0
    n_misses = 0

    for i in range(len(inputs)):
        if inputs[i].a == inputs[i].q:
            stat_dict['n_hits'] += 1
            total_hit_time += inputs[i].t
        else:
            total_miss_time += inputs[i].t
            n_misses += 1

        stat_dict['test_duration'] += inputs[i].t

    stat_dict['n_types'] = len(inputs)

    stat_dict['accuracy'] = stat_dict['n_hits'] / stat_dict['n_types'] if stat_dict['n_types'] != 0 else 0

    stat_dict['test_start'] = time.ctime(abs_b4_time)

    if not inputs:
        avg_type_time = 0
    else:
        avg_type_time = stat_dict['test_duration'] / len(inputs)
    
    stat_dict['type_avg_dur'] = '{:.3f}s'.format(avg_type_time)

    miss_avg_time = total_miss_time / n_misses if n_misses != 0 else 0
    stat_dict['miss_avg_dur'] = '{:.3f}s'.format(miss_avg_time)

    hit_avg_time = total_hit_time / stat_dict['n_hits'] if stat_dict['n_hits'] != 0 else 0
    stat_dict['hit_avg_dur'] = '{:.3f}s'.format(hit_avg_time)

    stat_dict['types'] = inputs

    return stat_dict

def main():
    parser = argparse.ArgumentParser(description='Script for testing typing speed and accuracy')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', default=False, help='Use timed mode: tests up to max_value seconds. Otherwise tests up to max_value letters')
    parser.add_argument('-mv', '--max_value', type=int, required=True, help='Number of seconds/letters of the test')
    parser.add_argument('-uw', '--use_words', action='store_true', default=False, help='Use word typing mode instead of single character typing (turned off by default)')
    args = parser.parse_args()

    inputs = []
    my_dict = {}

    if args.use_time_mode:
        TimedMode = True
    else:
        TimedMode = False

    if args.use_words:
        WordMode = True
    else:
        WordMode = False

    inputs, time_b4_exec = TypeTest(args.max_value, WordMode, TimedMode)
    my_dict = buildDict(inputs, time_b4_exec)

    print(Fore.GREEN + 'Your test statistics are:', '\n')
    for key, value in my_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()