import os

# assume ./a.out has already been made from get_boxes_raw.cpp

all_files = ["../part_data/p1/p1", "../part_data/p2/p2", "../part_data/p3/p3",\
        "../part_data/p4/p4", "../part_data/p5/p5", "../part_data/p6/p6",\
        "../part_data/p7/p7", "../part_data/p8/p8", "../part_data/p9/p9",\
        "../part_data/p10/p10", "../part_data/p11/p11"]

for file_prefix in all_files:
    print(file_prefix)
    command = f" ./a.out ../movie35c.asc {file_prefix}_l_ic.txt > "
    command += f"{file_prefix}_l_boxes_raw.txt" 
    os.system(command)

    command = f" ./a.out ../movie35c.asc {file_prefix}_r_ic.txt > "
    command += f"{file_prefix}_r_boxes_raw.txt" 
    os.system(command)
