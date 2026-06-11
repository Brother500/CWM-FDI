
import os

# Source - https://stackoverflow.com/a/42275253 Posted by Hrabal, modified by community. See post 'Timeline' for change history, Retrieved 2026-06-11, License - CC BY-SA 4.0
tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:]) 
mem_pc = round(used_m/tot_m,2)
print(mem_pc)

print(tot_m,used_m,free_m)


# Source - https://forums.raspberrypi.com/viewtopic.php?t=22180
def getCPUuse():
    CPUpc = 5
    return(str(os.popen("top -n1 | awk '/Cpu[(]s[)]:/ {print $2}'").readline().strip()))

CPU1 = getCPUuse()
print(CPU1)

# A Program to test the performance of a computer under load, record any bottlenecks
# or issues, and return solutions to any bottlenecks or issues.

#### Imports    ####

#### Variables  ####

# n = number of seconds to average over

#### Functions  ####

## Find CPU usage at one moment

## Find Memory usage at one moment

## Record CPU usage for n seconds
# Loop n times
#   Get CPU usage
#   Wait 1 second
# Return array of CPU usage

## Record Memory usage for n seconds
# Loop n times
#   Get Memory usage
#   Wait 1 second
# Return array of Memory usage

## Find avg of array
# Find length of array
# Find sum of array
# Find avg of array

#### Main code  ####

# Record CPU usage for n seconds
# Record Memory usage for n seconds
# Find avg CPU usage
# Find avg Memory usage
# Bottleneck if avg CPU usage > 95%
# Bottleneck if avg Memory usage > 80%
# Report any bottlenecks
# Propose solutions to bottlenecks

