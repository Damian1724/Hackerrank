#include <iostream>
#include<string>
#include <cstdio>
using namespace std;

int main() {
    string name[]={"one","two","three","four","five","six","seven","eight","nine"};
    int a,b;
    cin >> a;
    cin >> b;
    while(a <= b)
    {
        if(a >= 1 && a <=9)
        {
            cout << name[a-1] << endl;
        }
        else if(a%2==0)
        {
            cout << "even" << endl;
        }
        else
        {
            cout << "odd" << endl;
        }
        a++;
    }
    return 0;
}

