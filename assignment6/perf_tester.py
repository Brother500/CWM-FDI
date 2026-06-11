# A Program to test the performance of a computer under load, record any bottlenecks or issues, and return solutions to any bottlenecks or issues.

#### Imports    ####

import os
import time
import numpy as np

#### Variables  ####

n = 5               # n = number of seconds to average over

#### Functions  ####

## Find CPU usage at one moment
# Source - https://forums.raspberrypi.com/viewtopic.php?t=22180
def get_CPU_use():
    return(str(os.popen("top -n1 | awk '/Cpu[(]s[)]:/ {print $2}'").readline().strip()))

## Find Memory usage at one moment
# Source - https://stackoverflow.com/a/42275253 Posted by Hrabal, modified by community. See post 'Timeline' for change history, Retrieved 2026-06-11, License - CC BY-SA 4.0
def get_Memory_use():
    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    mem_pc = round(used_m/tot_m,2)
    return(mem_pc)

## Record CPU usage for n seconds
def record_CPU_usage(CPU_array,n):
    for i in range (0,n):           # Loop n times
        CPU_use_str = get_CPU_use()     # Get CPU usage
        time.sleep(1)               # Wait 1 second
        CPU_use = float(CPU_use_str)
        CPU_array.append(CPU_use)   # Add CPU usage to array
    return(CPU_array)# Return array of CPU usage

## Record Memory usage for n seconds
def record_Memory_usage(Memory_array,n):
    for i in range(0,n):                # Loop n times
        Memory_use = get_Memory_use()   # Get Memory usage
        time.sleep(1)                   # Wait 1 second
        Memory_array.append(Memory_use) # Add Memory usage to array
    return(Memory_array)                # Return array of Memory usage

## Find avg of array
def find_array_avg(array):
    array_length = len(array)               # Find length of array
    array_sum = np.sum(array)                  # Find sum of array
    array_avg = array_sum / array_length    # Find avg of array
    return(array_avg)


#### Main code  ####

CPU_bottleneck = False                                  # It is assumed that CPU and Memory are not bottlenecks until proven otherwise
Memory_bottleneck = False
CPU_usage = []
Memory_usage = []

CPU_usage = record_CPU_usage(CPU_usage,n)                         # Record CPU usage for n seconds
Memory_usage = record_Memory_usage(Memory_usage,n)                   # Record Memory usage for n seconds
CPU_avg = find_array_avg(CPU_usage)                     # Find avg CPU usage
Memory_avg = find_array_avg(Memory_usage)               # Find avg Memory usage
if CPU_avg >= 95:                                     # Bottleneck if avg CPU usage > 95%
    CPU_bottleneck = True
if Memory_avg >= 0.80:                                  # Bottleneck if avg Memory usage > 80%
    Memory_bottleneck = False
if CPU_bottleneck == True or Memory_bottleneck == True: # Report any bottlenecks
    if CPU_bottleneck == True:                          # Propose solutions to bottlenecks
        print("CPU usage averages over 95%! This is a bottleneck. Consider upgrading to a more powerful CPU.")
    if Memory_bottleneck == True:
        print("Memory usage averages over 80! This is a bottleneck. Consider upgrading to a larger amount of RAM.")
else:
    print("No bottlenecks! Try a more strenuous program.")
