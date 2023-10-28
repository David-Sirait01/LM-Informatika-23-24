/*
Latihan 2:
    Dalam studi kasus ini, program meminta pengguna untuk memasukkan
    usia dan memilih jenis tiket (A untuk dewasa, B untuk anak-anak).
    Program kemudian menentukan harga tiket berdasarkan jenis tiket
    dan usia. Harga tiket sesuai dengan aturan berikut:
    *   Tiket Dewasa (A) adalah $20 jika usia 18 tahun ke atas,
        atau $15 jika usia di bawah 18 tahun.
    *   Tiket Anak-Anak (B) adalah $15 jika usia 18 tahun ke atas,
        atau $10 jika usia di bawah 18 tahun.
*/

#include <iostream>
#include <cstdlib>

int main() {
    int usia;
    char type;
    std::cout << "Masukkan usia dan jenis tiket (Dipisahkan dengan spasi)\n>> ";
    std::cin >> usia >> type;

    // usia = 19;
    // type = 'a';
    int harga = 0;

    if (type == 'A' || type == 'a') {
        if (usia >= 18) {
            harga = 20;
        } else {
            harga = 15;
        }
    } else if (type == 'B' || type == 'b') {
        if (usia >= 18) {
            harga = 15;
        } else {
            harga = 10;
        }
    }

    std::cout << "Harga tiket " << type << " untuk usia " << usia << " adalah $" << harga;
    return EXIT_SUCCESS;
    
}
