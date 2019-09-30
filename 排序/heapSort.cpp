#include <iostream>
using namespace std;

void sift(int a[], int low, int high){
    int i, j, tmp;
    i = low;
    j = 2 * i + 1;
    tmp = a[low];
    while (j <= high){
        if (j+1 <= high && a[j] < a[j+1]){
            j = j + 1;
        }
        if (a[j] > tmp){
            a[i] = a[j];
            i = j;
            j = 2 * i + 1;
        } else{
            break;
        }
    }
    a[i] = tmp;
}

void heapSort(int a[], int n){
    int temp;
    for (int i=(n-2)/2; i>-1; i--){
        sift(a, i, n-1);
    }
    for (int j=n-1; j>-1; j--){
        temp = a[0];
        a[0] = a[j];
        a[j] = temp;
        sift(a, 0, j-1);
    }
}

int main(){
    int a[] = {4, 3, 6, 2, 8, 5, 7, 1, 9};
    int aLength;
    aLength = sizeof(a) / sizeof(int);
    for (int i=0; i<aLength; i++){
        cout << a[i] << ' ';
    }
    cout << endl;
    heapSort(a, aLength);
    for (int i=0; i<aLength; i++){
        cout << a[i] << ' ';
    }
}
