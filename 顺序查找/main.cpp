#include <iostream>
using namespace std;

int linear_search(int a[], int b){
    int a_length;
    a_length = sizeof(a) / sizeof(int);
    for (int i=0; i<a_length; i++) {
        if (a[i] == b)
            return i;
        }
    cout << "The number is not found! " << endl;
    return -1;
    }

int main() {
    int a[] = {1, 2, 3, 4, 5, 6};
    int b = 7;
    int index = linear_search(a, b);
    if (index != -1)
        cout << "The number's index is " << index <<endl;
    return 0;
}