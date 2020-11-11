import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

import get_ratios as rat
import to_temp


particles = ["../part_data/p1/p1", "../part_data/p2/p2", "../part_data/p3/p3",\
             "../part_data/p4/p4", "../part_data/p5/p5", "../part_data/p6/p6",\
             "../part_data/p7/p7", "../part_data/p8/p8", "../part_data/p9/p9",\
             "../part_data/p10/p10", "../part_data/p11/p11"]

NUM_PARTS = 11


# this function gets an array of temperature values for all particles
def get_temp_arr(ratios):

    # average the last frame value through space
    # there are NUM_PARTS particles

    # the number of frames should be 200
    num_frames = len(ratios[0])

    ave_ratio_for_N = np.zeros(NUM_PARTS)
    for i in range(0, NUM_PARTS):
        for j in range(0,  num_frames):
            ave_ratio_for_N[i] += ratios[i][j]

        ave_ratio_for_N[i] /= num_frames

    tot_ave_ratio = 0
    for i in range(0, NUM_PARTS):
        tot_ave_ratio += ave_ratio_for_N[i]

    tot_ave_ratio /= NUM_PARTS

    print("TOT AVE RATIO:")
    print(tot_ave_ratio)

    # calibration constant
    x = to_temp.get_const_val(tot_ave_ratio)

    print("CALIBRATION CONSTANT:")
    print(x)

    T = np.zeros((NUM_PARTS, num_frames))
    for i in range(0, NUM_PARTS):
        T[i] = to_temp.get_temp_spec_const(ratios[i], x)
        # UNCOMMENT TO PRINT ALL OF THE  TEMPS
        for j in range(0, num_frames):
            print(T[i][j])

    return T


def get_just_temp_arr(method):

    part = 0
    ratios = np.zeros((NUM_PARTS, 200))

    for file_prefix in particles:

        if method == "change_in_brightness":
            ratios[part] = rat.get_incr_ratios(file_prefix)
        elif method == "best_fit":
            all_ratios = rat.get_box_ratios(file_prefix)
            # RATIOS FOR BOX AREA NUM_PARTSxNUM_PARTS
            ratios[part] = all_ratios[2]

        part += 1

    # UNCOMMENT TO VIEW RATIO FOR EACH PARTICLE:
    # for i in range(0, NUM_PARTS):
        # print(f"PARTICLE: {i}")
        # print(ratios[i])

    T = get_temp_arr(ratios)

# print("Change In Brightness!")
# get_just_temp_arr("change_in_brightness")
# print("\nBF!")
get_just_temp_arr("best_fit")
