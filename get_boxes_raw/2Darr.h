#ifndef ARR2
#define ARR2

#include<iostream>

template <class T>
class Arr_2D{
public: 
    Arr_2D(int size){
        first_dim = size;
        data = new T*[first_dim](); 
    }

    Arr_2D(int size1, int size2){
        first_dim = size1;
        data = new T*[first_dim]();

        for(int i = 0; i < first_dim; i++)
            data[i] = new T[size2]();

    }

    ~Arr_2D(){
        for(int i = 0; i < first_dim; i++) {
            delete [] data[i];
        }

        delete [] data;
    }

    void set(int x, T *val){
        data[x] = val;
    }

    void set(int x, int y, T val){
        data[x][y] = val;
    }

    T at(int x, int y){
        return data[x][y];
    }

    int get_dim(int d) {
        if (d == 1) {
            return first_dim;
        }

        return second_dim;
    }

private:
    T **data;
    int first_dim;
    int second_dim;
};

#endif
