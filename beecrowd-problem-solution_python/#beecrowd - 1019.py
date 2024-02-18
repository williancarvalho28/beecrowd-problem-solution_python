# beecrowd - 1019
# Time Conversion

""" Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.
    Input
The input file contains an integer N.   
    Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds """

second = int(input())
hour = second//3600
second = second%3600
minutes = second//60
second = second%60

print(f'{hour}:{minutes}:{second}')