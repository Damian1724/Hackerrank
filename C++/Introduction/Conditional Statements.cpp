#include<iostream>
#include<string>
using namespace std;

int main()
{
    string name[] = {"one","two","three","four","five","six","seven","eight","nine"};
    int n;
    cin >> n;
    if (n >= 1 && n <= 9)
    {
        cout << name[n - 1] << endl;
    }
    else
    {
        cout << "Greater than 9" << endl;
    }
    system("pause");
    return 0;
}

