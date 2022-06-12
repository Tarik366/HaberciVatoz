#include <iostream>
#include <string>
using namespace std;

int main() {
    int a = 0;
    while (a < 10) {// var number of times to loop
        a += 1;
        string u= to_string(a);
        string h = string("MeteHan") + string(u) + string(", ");
        cout << h;
    }
    return 0;
}
