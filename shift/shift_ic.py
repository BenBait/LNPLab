import shift_func as shf
import numpy as np
import math
import sys

# all_files = ["./p1/p1", "./p2/p2", "./p3/p3", "./p4/p4", "./p5/p5", "./p6/p6",\
        # "./p7/p7", "./p8/p8", "./p9/p9", "./p10/p10"] 

all_files = ["../part_data/p10/p10"]
             #, "../part_data/p10/p10",
             # "../part_data/p11/p11", "../part_data/p12/p12"] 

for file_prefix in all_files:
    file = open(f"{file_prefix}_l_ic.txt")

    box = np.genfromtxt(file, dtype = int)

    shift_x = shf.shift(box[0], box[1])[0]
    shift_y = shf.shift(box[0], box[1])[1]

    prt_x = math.floor(shift_x)
    prt_y = math.floor(shift_y)
    original_stdout = sys.stdout

    with open(f'{file_prefix}_r_ic.txt', 'w') as n:
        sys.stdout = n
        print(str(prt_x) + " " + str(prt_y) + " " + str(box[2]) + " " + str(box[3]))
        sys.stdout = original_stdout
