//
// Created by qhp on 2019/9/29.
// C++中的int/int未整除，则向下取整
#include <iostream>
using namespace std;

void bubbleSort(int a[], int aLength) {
    int tmp;
    for (int i = 8; i > 1; i--){
        for (int j = 0; j < i; j++) {
            if (a[j] > a[j+1]){
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    }
}

int main(){
    int a[] = {4, 5, 3, 2, 6, 8, 7, 1, 9};
    int aLength;
    aLength = sizeof(a) / sizeof(int);
    bubbleSort(a, aLength);
    for (int i=0; i<9; i++){
        cout << a[i] << ' ';
    }
}
