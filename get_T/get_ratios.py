import numpy as np
import cib_int
import bf_int

NUM_TOT_FRAMES = 288
NUM_FRAMES     = 200     # number of frames used for calculation
NUM_BOXES      = 8

# START BEST FIT RATIOS
def get_box_ratios(to_open):

    coeff_r = bf_int.get_coeffs("../bg_info/right_bg_data.txt")
    coeff_l = bf_int.get_coeffs("../bg_info/left_bg_data.txt")

    # seperate data into 288 arrays of 8 intensity values, where each intensity
    # value is the intensity of a box
    file = open(to_open + "_l_boxes_raw.txt")
    data_l = np.genfromtxt(file, dtype=int)
    by_slide_l = np.split(data_l, NUM_TOT_FRAMES)

    file = open(to_open + "_r_boxes_raw.txt")
    data_r = np.genfromtxt(file, dtype=int)
    by_slide_r = np.split(data_r, NUM_TOT_FRAMES)

    # NOTE: 8 is the number of BOXES, NOT PARTICLES
    ratio = np.zeros((NUM_BOXES, NUM_FRAMES))

    for i in range(NUM_TOT_FRAMES - NUM_FRAMES, NUM_TOT_FRAMES):
        left_int = np.zeros(NUM_BOXES)
        right_int = np.zeros(NUM_BOXES)

        for k in range(0, NUM_BOXES):
            x_l = by_slide_l[i][k][0]
            y_l = by_slide_l[i][k][1]
            w_l = by_slide_l[i][k][2]
            h_l = by_slide_l[i][k][3]
            left_int[k] = by_slide_l[i][k][4]

            x_r = by_slide_r[i][k][0]
            y_r = by_slide_r[i][k][1]
            w_r = by_slide_r[i][k][2]
            h_r = by_slide_r[i][k][3]
            right_int[k] = by_slide_r[i][k][4]

            if not w_l == w_r:
                print("IMPROPER SIZES")

            for l in range(0, h_l):
                for m in range(0, w_l):
                    # ADD to x and y null because we move DOWN and RIGHT through
                    # the box as the background is subtracted
                    right_int[k] -= bf_int.best_fit(coeff_r, i, x_r + m, y_r + l)
                    left_int[k] -= bf_int.best_fit(coeff_l, i, x_l + m, y_l + l)

            ratio[k][i - 88] = right_int[k] / left_int[k]

    return ratio


# START INCREASE RATIOS
def get_incr_ratios(file_prefix):

    num_frames = 200
    sides = ["_l", "_r"]
    ave_ratios_per_part = np.zeros(10)
    bands = np.zeros((2, num_frames))

    for side in sides:
        side_and_part = file_prefix + side
        box_intensities = cib_int.get_box_ints(side_and_part)

        part_int = np.zeros(num_frames)

        for i in range(88, 288):
            for j in range(4, 8):
                part_int[i - 88] += box_intensities[i][j]

            part_int[i - 88] /= 4

            if side == "_l":
                bands[0][i - 88] = part_int[i - 88]
            else:
                bands[1][i - 88] = part_int[i - 88]

    ratios = np.zeros(num_frames)
    ave_ratio = 0
    for i in range(0, num_frames):
        ratios[i] = bands[1][i] / bands[0][i]

    ave_ratios_add_frame = np.zeros(num_frames)

    for i in range(0, num_frames):
        for j in range(0, i + 1):
            ave_ratios_add_frame[i] += ratios[j]

        ave_ratios_add_frame[i] /= (i + 1)

    return ave_ratios_add_frame


def get_incr_ratio_space(ave_ratios_per_part, order):
    sum_ave = np.zeros(8)

    for i in range(0, 8):
        for j in range(0, i + 1):
            sum_ave[i] += ave_ratios_per_part[order[j]]

        sum_ave[i] /= (i + 1)

    return sum_ave
