#include <iostream>

/*
    Latihan:
    Dalam studi kasus ini, program akan meminta pengguna untuk memasukkan pendapatan dan jumlah tahun layanan karyawan.
    Berdasarkan aturan bisnis, program akan menghitung bonus gaji karyawan. Aturan yang digunakan adalah:

    Jika pendapatan lebih dari $50,000 dan karyawan telah bekerja selama 5 tahun atau lebih, bonus adalah 10% dari pendapatan.
    Jika pendapatan lebih dari $50,000 dan karyawan telah bekerja kurang dari 5 tahun, bonus adalah 5% dari pendapatan.
    Jika pendapatan kurang dari atau sama dengan $50,000, bonus adalah 2% dari pendapatan.
*/

double percent_of(double var, double perc) {
    double num = (perc / 100);
    double result = num * var;
    return result;
}

int main() {
    double var, yr, bonus = 0;
    std::cout << "Masukkan gaji dan tahun (dipisahkan dengan spasi): ";
    std::cin >> var >> yr;

    if (var >= 50000 && yr > 5)
    {
        bonus = 10;
    }
    else if (var >= 50000 && yr <= 5)
    {
        bonus = 5;
    }
    else if (var <= 50000)
    {
        bonus = 2;
    }

    double bonus_val = percent_of(var, bonus);
    double total = var + bonus_val;

    std::cout << "Gaji awal: $" << var << std::endl;
    std::cout << bonus << "% bonus: $" << bonus_val << std::endl;
    std::cout << "Total gaji: $" << total_salary << std::endl;

    return 0;
}