//
// Created by qhp on 2019/9/29.
// C++中的int/int未整除，则向下取整
#include <iostream>
using namespace std;

void selectSort(int a[], int aLength){
    int tmp;
    for (int i=0; i<aLength-1; i++){
        for (int j=i+1; j<aLength; j++){
            if (a[i] > a[j]){
                tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
        }
    }
}

int main(){
    int a[] = {4, 5, 3, 2, 6, 8, 7, 1, 9};
    int aLength;
    aLength = sizeof(a) / sizeof(int);
    selectSort(a, aLength);
    for (int i=0; i<9; i++){
        cout << a[i] << ' ';
    }
}
