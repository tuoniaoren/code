//
// Created by qhp on 2019/9/29.
// C++中的int/int未整除，则向下取整
#include <iostream>
using namespace std;

int partition(int a[], int left, int right){
    int tmp;
    tmp = a[left];
    while (left < right){
        while (left < right && a[right] > tmp){
            right--;
        }
        a[left] = a[right];
        while (left < right && a[left] < tmp){
            left++;
        }
        a[right] = a[left];
    }
    return left;
}

void fastSort(int a[], int left, int right) {
    int mid;
    if (left < right){
        mid = partition(a, left, right);
        fastSort(a, left, mid-1);
        fastSort(a, mid+1, right);
    }
}

int main(){
    int a[] = {4, 5, 3, 2, 6, 8, 7, 1, 9};
    int aLength;
    aLength = sizeof(a) / sizeof(int);
    fastSort(a, 0, aLength-1);
    for (int i=0; i<9; i++){
        cout << a[i] << ' ';
    }
}
