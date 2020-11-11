/* 
 * This method is for finding the change in x and in y for a series of data
 * points collected by "hand"
 */
#include<iostream>
#include<fstream>
#include<vector>

void open_get_delta(std::string);

int main(int argc, char *argv[]){
    if(argc < 2){
        std::cerr << "Please specify an argument\n";
        return 1;
    }

    std::string shift_data = argv[1];

    open_get_delta(shift_data);

    return 0;
}

void open_get_delta(std::string data){
    std::fstream infile;
    infile.open(data);

    if(!infile.is_open()){
        std::cerr << "Error opening data file\n";
    }

    std::vector<int> x, y, x_, y_;
    int temp;

    while(!infile.eof()){
        infile >> temp;
        x.push_back(temp);
        infile >> temp;
        y.push_back(temp);
        infile >> temp;
        x_.push_back(temp);
        infile >> temp;
        y_.push_back(temp);
    }

    /* pop off EOF char */
    x.pop_back();
    y.pop_back();
    x_.pop_back();
    y_.pop_back();
    
    int elems = x.size();
    int deltas[2][elems];

    for(int i = 0; i < elems; i++){
        deltas[0][i] = x_[i] - x[i];
        deltas[1][i] = y_[i] - y[i];
    }

    for(int i = 0; i < elems; i++)
        std::cout << x[i] << std::endl;

    for(int i = 0; i < elems; i++)
        std::cout << y[i] << std::endl;

    for(int i = 0; i < 2; i++)
        for(int j = 0; j < elems; j++)
            std::cout << deltas[i][j] << std::endl;
}
