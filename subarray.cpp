#include<iostream>
#include<vector>
using namespace std;[1,2,3,-1,5,1,1]

int main (){
int i,n,value;
int maxSum=0,tempSum=0;
vector <int> a;
vector <int> maxSumArray;
vector <int> tempArray;
cout<<"enter the length of array = ";  
cin>>n;
cout<<"enter the array = \n";
for(i=0;i<n;i++) {
    cin>>value;
    a.push_back(value);
}
for (i=0;i<n;i++) {
    if(a[i]>=0){
            tempArray.push_back(a[i]);      
            tempSum=tempSum+a[i];
                                    
        }else{
            if(tempSum>maxSum){
                maxSum=tempSum;
                maxSumArray=tempArray;
            }
            else if(tempSum==maxSum && tempArray.size()>maxSumArray.size()){
                maxSumArray=tempArray;
            
            }
            tempSum=0;
            tempArray.clear();}
        }

         if(tempSum>maxSum){
                maxSum=tempSum;
                maxSumArray=tempArray;
            }
             else if(tempSum==maxSum && tempArray.size()>maxSumArray.size()){
                maxSumArray=tempArray;
            
            }

        
        cout<<"max sum array";
        for(i=0;i<maxSumArray.size();i++){
        cout<< maxSumArray[i];
        }
        cout<<"max sum";
        cout<< maxSum;
  



    return 0;
}