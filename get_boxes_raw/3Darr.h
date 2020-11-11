#ifndef ARR_3D
#define ARR_3D

#include<iostream>

template <class T>
class Arr_3D{
public:
    Arr_3D(int dim_1, int dim_2, int dim_3){
        set(dim_1, dim_2, dim_3);
    }

    ~Arr_3D(){ delete [] arr; }

    void populate(int s, int x, int y, int in){
        arr[s + x*depth + y*depth*width] = in;
    }

    int at(int s, int x, int y){
        return arr[s + x*depth + y*depth*width];
    }

private:
    void set(int dim_1, int dim_2, int dim_3){
        depth = dim_1;
        width = dim_2;
        height = dim_3;
        size = depth * width * height;
        arr = new int[size]();
    }

    int depth, width, height;
    int size;
    int *arr;
};

#endif
