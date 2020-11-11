# This file has the functions for getting the coefficients for the best fit
# equation and then another function for finding the anticipated intensity at
# at the specified pixel

import numpy as np
import scipy.linalg


NUM_TOT_FRAMES = 288
NUM_COEFFS     = 6


def get_coeffs(file_name):
    file = open(file_name)

    bg_data = np.genfromtxt(file, dtype=int)

    axis = np.split(bg_data, NUM_TOT_FRAMES + 2)

    #x and y axis are the same for every slide
    x = axis[0]
    y = axis[1]

    indiv_bg_data = np.zeros((NUM_TOT_FRAMES, NUM_COEFFS))

    for i in range(0, NUM_TOT_FRAMES):
        z = axis[i]
        data = np.c_[x, y, z]
        A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
        C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])

        # Z is the best fit surface, in case you want to graph it or something
        # Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)

        indiv_bg_data[i][0] = C[4]
        indiv_bg_data[i][1] = C[5]
        indiv_bg_data[i][2] = C[3]
        indiv_bg_data[i][3] = C[1]
        indiv_bg_data[i][4] = C[2]
        indiv_bg_data[i][5] = C[0]

    return indiv_bg_data


#i is the slide index
def best_fit(a, i, x, y):
    return a[i][0]*x**2 + a[i][1]*y**2 + a[i][2]*x*y + a[i][3]*x + a[i][4]*y \
           + a[i][5]
