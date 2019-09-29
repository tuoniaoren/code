#include <iostream>
using namespace std;

void insertionSort(int a[], int aLength){
    int tmp,i,j;
    i = 1;
    while (i < aLength){
        tmp = a[i];
        j = i - 1;
        while (j>=0){
            if (a[j] > tmp){
                a[j+1] = a[j];
                j--;
            }
            else
                break;
        }
        a[j+1] = tmp;
        i++;
    }
}

int main(){
    int a[] = {4, 5, 3, 2, 6, 8, 7, 1, 9};
    int aLength;
    aLength = sizeof(a) / sizeof(int);
    insertionSort(a, aLength);
    for (int i=0; i<9; i++){
        cout << a[i] << ' ';
    }
}