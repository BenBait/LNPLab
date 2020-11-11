/*****************************************************************************
    This program reads in the .asc value of the .sif movie and converts it into
    a 3D array. The passed particle initial conditions are then used to
    construct boxes of increasing sizes around the particle.
    By Ben Maloy
******************************************************************************/
#include<iostream>
#include<fstream>

#include"3Darr.h"
#include"2Darr.h"
#include"open_make_box.h"

#define B 8 //number of boxes

int calculate(Arr_3D<int> &arr, std::string calc_ic);

//PASS IN ASCII VALUES AND PARTICLE INITIAL CONDITIONS
int main(int argc, char *argv[]){
	if(argc < 3){
	    std::cerr << "Please specify two arguments\n";
		return 1;
	}

	std::string image_file = argv[1];
    std::string calc_ic = argv[2];

    //arr[S][X][Y] --> There are S 512 by 512 images
    Arr_3D<int> arr(S, X, Y);


    // populate array function is from the open_make_box header
    if(!populate_arr(image_file, arr)){
        std::cerr << "ERROR: The initial data structure was not populated!\n";
        return 1;
    }

	return calculate(arr, calc_ic);
}

int calculate(Arr_3D<int> &arr, std::string calc_ic){
    std::fstream infile;
    infile.open(calc_ic);

    if(!infile.is_open()){
        std::cerr << "ERROR OPENING FILE\n";
        return 1;
    }

    // These are the conditions for the first box
    int x_null;
    int y_null;
    int h_null;
    int w_null;

    infile >> x_null >> y_null >> h_null >> w_null;

    Arr_2D<int> measurements_raw(B, S);

    // S is the number of frames and B is the number of boxes
    // so the total intensity inside each box for this particle at every slide
    // will be printed
    for(int l = 0; l < S; l++){
        for(int j = 0, k = 0; j < B; j++, k+=2){
            // SUBTRACT from x and y null because we move the box UP and LEFT
            // compare to lines 49 & 50 in get_ratios which moves DOWN and RIGHT
            int *to_set = make_box(arr, x_null - j, y_null - j, w_null + k, h_null + k);
            measurements_raw.set(j, to_set);

            std::cout << x_null - j << " " << y_null - j << " "  << w_null + k;
            std::cout << " "  << h_null + k << " ";
            std::cout << measurements_raw.at(j, l) << std::endl;
        }
    }

    return 0;
}
