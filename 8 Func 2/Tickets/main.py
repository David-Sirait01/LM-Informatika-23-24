"""
Latihan 2:
    Dalam studi kasus ini, program meminta pengguna untuk memasukkan
    usia dan memilih jenis tiket (A untuk dewasa, B untuk anak-anak).
    Program kemudian menentukan harga tiket berdasarkan jenis tiket
    dan usia. Harga tiket sesuai dengan aturan berikut:
    *   Tiket Dewasa (A) adalah $20 jika usia 18 tahun ke atas,
        atau $15 jika usia di bawah 18 tahun.
    *   Tiket Anak-Anak (B) adalah $15 jika usia 18 tahun ke atas,
        atau $10 jika usia di bawah 18 tahun.
"""

def main():
    input_str = input("Masukkan usia dan jenis tiket (Dipisahkan dengan spasi)\n>> ")
    usia, jenis = map(str, input_str.split())
    
    usia = int(usia)
    harga = 0

    if jenis in ("A", "a") and usia >= 18:
        harga = 20
    elif jenis in ("A", "a") and usia < 18:
        harga = 15
    elif jenis in ("B", "b") and usia >= 18:
        harga = 15
    elif jenis in ("B", "b") and usia < 18:
        harga = 10

    print(f"Harga tiket {jenis} untuk usia {usia} adalah ${harga}")

main()

