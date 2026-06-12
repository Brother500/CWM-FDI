# A Program to test the performance of a computer under load, record any bottlenecks or issues, and return solutions to any bottlenecks or issues.

#### Imports    ####

import os
import time
import numpy as np

#### Variables  ####

n = 10              # Number of samples to average over
i = .01             # Time between samples in seconds

#### Functions  ####

## Get CPU usage at one moment
# Source - https://stackoverflow.com/a/59214241
# Posted by Giammo
# Retrieved 2026-06-12, License - CC BY-SA 4.0
def get_CPU_use():
    return(str(os.popen("top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}'").readline().strip())) 


## Get Memory usage at one moment as a percentage
# Source - https://stackoverflow.com/a/42275253
# Posted by Hrabal, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-11, License - CC BY-SA 4.0
def get_Memory_use():
    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])    # Find Memory capacity, Memory in use, & Memory free
    mem_pc = 100*round(used_m/tot_m,2)                                                      # Find percentage of Memory capacity that is in use
    return(mem_pc)

## Record CPU usage n times, i seconds apart, as float values in CPU_array
def record_CPU_usage(CPU_array,n,i):
    for j in range (0,n):               # Loop n times
        CPU_use_str = get_CPU_use()     # Get CPU usage
        time.sleep(i)                   # Wait i (interval) seconds
        CPU_use = float(CPU_use_str)    # Convert to float for use in calculations
        CPU_array.append(CPU_use)       # Add CPU usage to array
    return(CPU_array)                   # Return array of CPU usage

## Record Memory usage n times, i seconds apart, in Memory_array
def record_Memory_usage(Memory_array,n,i):
    for j in range(0,n):                # Loop n times
        Memory_use = get_Memory_use()   # Get Memory usage
        time.sleep(i)                   # Wait i (interval) seconds
        Memory_array.append(Memory_use) # Add Memory usage to array
    return(Memory_array)                # Return array of Memory usage

## Find average value of array, and return this value
def find_array_avg(array):
    array_length = len(array)               # Find length of array
    array_sum = np.sum(array)               # Find sum of array
    array_avg = array_sum / array_length    # Find average of array
    return(array_avg)


#### Main code  ####

CPU_bottleneck = False      # It is assumed that CPU and Memory are not bottlenecks until proven otherwise
Memory_bottleneck = False
CPU_usage = []              # Initialise empty arrays for CPU & Memory usage
Memory_usage = []

CPU_usage = record_CPU_usage(CPU_usage,n,i)                 # Record CPU usage n times, i seconds apart
Memory_usage = record_Memory_usage(Memory_usage,n,i)        # Record Memory usage n times, i seconds apart
CPU_avg = find_array_avg(CPU_usage)                         # Find average CPU usage
Memory_avg = find_array_avg(Memory_usage)                   # Find average Memory usage
print("CPU average % is:", CPU_avg, "Memory average % is", Memory_avg)
if CPU_avg >= 95:                                           # Bottleneck if average CPU usage > 95%
    CPU_bottleneck = True
if Memory_avg >= 80:                                        # Bottleneck if average Memory usage > 80%
    Memory_bottleneck = True
if CPU_bottleneck == True and Memory_bottleneck == True:    # If both are high, neither is a bottleneck
    print("Both CPU and Memory are utilised well, neither is a bottleneck for this program.")
else:
    if CPU_bottleneck == True:                              # Report & propose solutions to bottlenecks
        print("CPU usage averages over 95%! This is a bottleneck. Consider upgrading to a more powerful CPU.")
    elif Memory_bottleneck == True:
        print("Memory usage averages over 80%! This is a bottleneck. Consider closing tabs and programs that are not in use or upgrading to a larger amount of RAM.")
    else:                                                   # Neither is high so cannot tell if there is a bottleneck
        print("Not enough load to tell if there is a bottleneck. Try a more strenuous program.")
