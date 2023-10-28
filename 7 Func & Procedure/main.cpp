#include <iostream>
#include <windows.h>

using namespace std;

class SQ {
    public:
    int p, l;

    public:
        class Func {
        public:
            int luas(int p, int l) {
                return p * l;
            }

            int keliling(int p, int l) {
                return (2 * p) + (2 * l);
            }
        } functions;

        class Proc {
        public:
            void keliling(int s) {
                int result = s * 4;
                cout << "Keliling = " << result << " satuan" << endl;
            }

            void luas(int s) {
                int result = s * s;
                cout << "Luas = " << result << " satuan" << endl;
            }
        } procedures;
};

int main() {
    cout << "Starting . . .\n\n";
    Beep(750, 500);

    SQ block;
    int var = 4;
    cout << "Test case = " << var << "\n\n";
    block.p = var;
    block.l = var;

    cout << "// Func\n";
    cout << "Luas: " << block.functions.luas(block.p, block.l) << " satuan" << endl;
    cout << "Keliling: " << block.functions.keliling(block.p, block.l) << " satuan" << endl;

    cout << "\n// Procedure\n";
    block.procedures.keliling(var);
    block.procedures.luas(var);

    return 0;
}
