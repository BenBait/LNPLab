import numpy as np


# EQN: (Ratio - constant) / 0.013


# get constant given the whole array
def get_const_rat(ratios):

    size = len(ratios)
    temp = np.zeros(size)

    tot_ave = ratios[size - 1]

    x = tot_ave - (35 * 0.013)

    return x

# get constant with the total average ratio value
def get_const_val(tot_ave):

    x = tot_ave - (35 * 0.013)

    return x

def get_temp(ratio):

    size = len(ratio)
    temp = np.zeros(size)

    tot_ave = ratio[size - 1]

    x = tot_ave - (35 * 0.013)

    # print("CONSTANT: " + str(round(x,4)))

    for i in range(0, size):
        temp[i] = (ratio[i] - x) / 0.013

    return temp

def get_temp_spec_const(ratio, x):

    size = len(ratio)
    temp = np.zeros(size)

    for i in range(0, size):
        temp[i] = (ratio[i] - x) / 0.013

    return temp

def get_single_temp_spec_const(ratio, x):

    temp = (ratio - x) / 0.013

    return temp
