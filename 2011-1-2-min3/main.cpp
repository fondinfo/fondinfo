#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int a, b, c, min;

    cout << "Insert three numbers: ";
    cin >> a >> b >> c;

    if (a < b && a < c) {
        min = a;
    } else if (b < c) {
        min = b;
    } else {
        min = c;
    }

    cout << "Minimum: " << min << endl;

    return 0;
}
