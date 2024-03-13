//write a program to strcpy "HCL Technologies" to "HCL Technologies India"
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char str1[] = "HCL Technologies";
    char str2[] = " India";
    //concenate str1, str2 and print before and after
    cout << "Before: " << str1 << endl;
    strcat(str1, str2);
    cout << "After: " << str1 << endl;
    return 0;
}