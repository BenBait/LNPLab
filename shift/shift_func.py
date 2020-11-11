import numpy as np
import scipy.linalg

path = "./deltas.out"
file = open(path)

all_data = np.genfromtxt(file, dtype = int)

axis = np.split(all_data, 4)
x_ = axis[0]
y_ = axis[1]

def shift_eqn():
    # Produces equations of the form: 
    # Z = C[4]*X**2 + C[5]*Y**2 + C[3]*X*Y + C[1]*X + C[2]*Y + C[0]
    z = axis[2]
    data = np.c_[x_,y_,z] 
    A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
    C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])
    x_shift = np.array([C[4], C[5], C[3], C[1], C[2], C[0]])

    z = axis[3]
    data = np.c_[x_,y_,z] 
    A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
    C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])
    y_shift = np.array([C[4], C[5], C[3], C[1], C[2], C[0]])

    return x_shift, y_shift

def shift(x, y):
    x_coeff = shift_eqn()[0]
    y_coeff = shift_eqn()[1]
    
    delta_x = x_coeff[0]*x**2 + x_coeff[1]*y**2 + x_coeff[2]*x*y + x_coeff[3]*x + x_coeff[4]*y + x_coeff[5]
    delta_y = y_coeff[0]*x**2 + y_coeff[1]*y**2 + y_coeff[2]*x*y + y_coeff[3]*x + y_coeff[4]*y + y_coeff[5]

    new_x = round(x + delta_x)
    new_y = round(y + delta_y)

    return new_x, new_y
