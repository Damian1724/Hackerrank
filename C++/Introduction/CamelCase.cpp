#include<iostream>
#include<string>
using namespace std;


int main()
{
    string input;
    cin >> input;
    int total = 1;
    for (int i = 0; i < input.length(); i++)
    {
        if (int(input[i]) >= 65 && int(input[i]) <= 90)
        {
            total += 1;
        }
    }
    cout << total << endl;
    system("pause");
    return 0;
}

