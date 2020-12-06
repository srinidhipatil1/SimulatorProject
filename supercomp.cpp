#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

//create function
int main() 
{ 
    // file pointer 
    fstream fout; 
  
    // opens an existing csv file or creates a new file. 
    fout.open("covid.csv", ios::out | ios::app);
    fout<<"age, DurationOfTreatment, CostOfTreatment, DidTheyDie"<<endl; 
  
     
  
    int age, DurationOfTreatment, DidTheyDie; //1= Alive,  0= deceased
    long CostOfTreatment;
    
    // Read the input 
    for (int i = 0; i < 50; i++) { 
        /*int range = max - min + 1;
        int num = rand() % range + min;
        this is used to generate random numbers within a range*/
        age= rand() % 79+2; //min=2, max=80
        DurationOfTreatment= rand() % 13+1; //min=1, max=14
        if (DurationOfTreatment<8){
            CostOfTreatment=rand() % 60001+40000; 
        }
        else{
            CostOfTreatment=rand() % 100001+100000; //to give sense to the data
        }
        if(age>75 && DurationOfTreatment>11){
            DidTheyDie=1;    //to give sense to the data
        }
        else
        {
            DidTheyDie= rand() % 2;
        }
        fout<<age<<",";
        fout<<DurationOfTreatment<<",";
        fout<<CostOfTreatment<<",";
        fout<<DidTheyDie<<endl;
    } 
} 