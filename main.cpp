#include <iostream>
#include <string>
using namespace std;

int main() {
    int a = 0;
    while (a < 7) {// var number of times to loop
        a += 1;
        string u= to_string(a);
        string h = string("Metehan") + string(u) + string(", ");
        cout << h;
    }
    return 0;
}
