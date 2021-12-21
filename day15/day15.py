#!/usr/bin/python3
'''
  Day 14 part 1
'''
#import re
import numpy as np

#IF = open("../day15.data")
IF = open("../day15.demo")

STARTX = 0
STARTY = 0
MAP = []
VISITED_MAP = []
CURR_MIN = 0

def print_list(my_list):
    '''
    A stupid function to print a list by element
    '''
    for element in my_list:
        print(element)

def walk_map( cur_x, cur_y):
    '''
    Here is where I walk through the maze
    '''
    print("Looking at (%d, %d)" % (cur_x, cur_y))
    return 0

def main():
    '''
    Here be the start of dragons
    '''
    lines = IF.readlines()

    for line in lines:
        line = line.rstrip("\r\n")
        print("Line: %s"%(line))
        row = np.zeros(len(line), dtype=int)
        #for i in range(len(line)):
        #    row[i] = int(line[i])
        for count, value in enumerate(line):
            row[count] = int(value)
        MAP.append(row)
        VISITED_MAP.append(np.zeros(len(line), dtype=int))


    print("Risk Map")
    print_list(MAP)
    print("Visited Map")
    print_list(VISITED_MAP)
    m_v = np.amax(MAP)
    print("Max value: %d" %(m_v))

    CURR_MIN = len(MAP) + len(MAP[0]) - 1

    walk_map(0,0)

if __name__ == "__main__":
    main()
