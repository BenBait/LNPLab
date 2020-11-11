# This file contains functions to find the average intensity added and uses it
# to predict the bg value around a particle
# Also subtracts the CIB bg from the particle with the last function
import numpy as np
# import bg_increase as bg

# Use 4 intensities added (where plateau is reached) as a prediction for the
# average background of all of the pixels inside of the larges box


def get_bg(a):
    bg = 0
    for i in range(3, 7):
        bg += a[i]

    bg /= 4

    return bg


def get_brightness(by_slide):
    brightness = np.zeros(288)
    bg = np.zeros(288)

    for i in range(0, 288):
        ave_added = np.zeros(7)
        # 7 additions happen (8 boxes)
        for j in range(0, 7):
            start = by_slide[i][j][4]
            added_int = by_slide[i][j + 1][4] - start

            area_1 = by_slide[i][j][2] * by_slide[i][j][3]
            area_2 = by_slide[i][j + 1][2] * by_slide[i][j + 1][3]
            area_added = area_2 - area_1

            ave_added[j] = added_int / area_added

        bg[i] = get_bg(ave_added)

        area_last = by_slide[i][7][2] * by_slide[i][7][3]

        brightness[i] = by_slide[i][7][4] - (bg[i] * area_last)

    return brightness, bg


def get_brightness_added(by_slide):
    # ave_added refers to the average pixel brightness added
    ave_added = np.zeros((288, 7))

    for i in range(0, 288):
        # 7 additions happen (8 boxes)
        for j in range(0, 7):
            start = by_slide[i][j][4]
            added_int = by_slide[i][j + 1][4] - start

            area_1 = by_slide[i][j][2] * by_slide[i][j][3]
            area_2 = by_slide[i][j + 1][2] * by_slide[i][j + 1][3]
            area_added = area_2 - area_1

            ave_added[i][j] = added_int / area_added

    return ave_added

# this function returns the values of the intensity of the box minus the
# background times the area
def get_box_ints(to_open):
    file = open(to_open + "_boxes_raw.txt")

    data = np.genfromtxt(file, dtype=int)

    by_slide = np.split(data, 288)

    backg = get_brightness(by_slide)[1]

    subtracted = np.zeros((288, 8))

    for i in range(0, 288):

        for j in range(0, 8):
            x = by_slide[i][j][0]
            y = by_slide[i][j][1]
            w = by_slide[i][j][2]
            h = by_slide[i][j][3]
            raw = by_slide[i][j][4]

            area = w * h

            raw -= (backg[i] * area)

            subtracted[i][j] = raw

    return subtracted
