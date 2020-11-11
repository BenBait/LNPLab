/*
 * This head contains a method for coverting the ascii values to a 3D array
 * and one for drawing the boxes and gathering the brightness from this array.
 */
#ifndef OPEN_MAKE_BOX
#define OPEN_MAKE_BOX

#include<iostream>
#include<fstream>
#include"2Darr.h"
#include"3Darr.h"

#define S 288 //# of pics
#define X 512
#define Y 512

//Put the ascii values in the 3d array
bool populate_arr(std::string file, Arr_3D<int> &arr){
	int index[S][X]; //The first number in every row is an index for that row
    std::fstream infile;
    infile.open(file);

	if(!infile.is_open()){
		std::cerr << "Error opening ascii file";
		return false;
	}
    
    int *temp = new int[S * X * Y]();

    for(int i = 0; i < S; i++){
        for(int j = 0; j < X; j++){
            //capture the index then proceed to make the 2D array
            infile >> index[i][j];

            for(int k = 0; k < Y; k++){
                infile >> temp[i + j + k];
                arr.populate(i, j, k, temp[i + j + k]);
            }
        }
    }

    delete [] temp;
    return true;
}

//Calculate the intensity of the given rectangle
int *make_box(Arr_3D<int> &arr, int x_null, int y_null, int w, int h){
    //arr is the 3d array of pixel intensity values
    int *val = new int[S]();

    for(int i = 0; i < S; i++){
        for(int j = 0; j < w; j++){
            for(int k = 0; k < h; k++){
                val[i] += arr.at(i, x_null + j, y_null + k);
            }
        }
    }

    return val;
}

#endif
