import numpy as np
import sys

if __name__ == "__main__":
    # mode file
    mode = open(sys.argv[1], 'r')
    lines = mode.readlines()
    # lines of one frame
    frame_lines = 814
    frame_index = 38
    start = frame_index * frame_lines
    end = start + frame_lines
    for i in range(start, end):
        line = lines[i]
        print(line, end="")
    pass