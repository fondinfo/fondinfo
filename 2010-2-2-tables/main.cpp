#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    int x, y;

    for (y = 1; y <= 10; ++y) {

        for (x = 1; x <= 10; ++x) {
            cout << setw(4) << x * y;
        }
        cout << endl;

    }

    return 0;
}
