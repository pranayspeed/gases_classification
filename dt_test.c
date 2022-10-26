#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

#include <math.h>
#include <sstream>



#include "DecisionTree_unprocessed.h"

int predict_class(float *x)
{  
    return predict(x); 
}


int main(int argc, char *argv[])
{

    string full_path = "./test_output_unprocessed.csv";

    string full_path_res = "./test_results.txt";
    ofstream out_file;
    out_file.open(full_path_res,  std::ofstream::out);

    int n,i;
    n = 32;

    int limit = 5000;
    float X_data[32] = {0};
    int target = 0;
    ifstream inFile;

    inFile.open(full_path);
    

    string line;
    
    while (limit!=0)
    {
        getline(inFile, line);
        stringstream s(line);
        string word;
        i=0;
        //std::cout<< line <<"\n ";
        while (getline(s, word, ',')) 
        {
            
            if (i==32)
            {
                target = stoi(word);
                //std::cout<<"target: "<< target <<"    ";

            }
            else{
                        // add all the column data
            // of a row to a vector
            X_data[i] = stof(word.c_str());
            //std::cout<< X_data[i] <<" ";
            }
            i++;


        }

        // Process the data for decision
        int y_pred = predict_class(X_data);
        //std::cout<<"\t Predicted: "<< y_pred <<"\n";
        out_file << y_pred <<endl;
        limit--;


    }


    out_file.close();
    inFile.close();



    return 0;
}