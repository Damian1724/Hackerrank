#include<iostream>
#include<string>
#include <iomanip> 
using namespace std;


int main()
{
    int n;
    string answer = "#";
    cin >> n;
    for (int i = 0; i < n; i++)
    {

        cout << setw(n) << answer << endl;
        answer += "#";
    }
    system("pause");
    return 0;
}

