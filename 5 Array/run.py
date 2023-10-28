import os, sys, time, threading
from colorama import Fore, Back, init

s_stop = threading.Event()

init(autoreset=True)

def printmid(text, color, p=True):
    # Mendapatkan lebar terminal saat ini
    terminal_width = os.get_terminal_size().columns

    # Menghitung panjang teks yang akan ditampilkan
    text_length = len(text)

    # Menghitung jumlah karakter "-" yang diperlukan untuk mengelilingi teks
    border_length = (terminal_width - text_length - 4) // 2  # 4 adalah untuk tanda "="

    # Membuat garis batas atas
    top_border = "=" * border_length

    # Membuat garis batas bawah
    bottom_border = "=" * (border_length + (text_length % 2))  # Menambahkan satu "=" jika panjang teks ganjil

    # Menampilkan teks di tengah layar dengan batasan atas dan bawah
    content = color + top_border + f"[{text}]" + bottom_border + "\n"
    if p == True:
        print(content)
        return content
    else:
        return content


finished = False
def compile():
    global finished
    # print(Back.BLUE + "Compiling C++", end="")
    os.system(r"g++ -o main main.cpp")
    finished = True

def dots():
    i = 0
    while not finished:
        i = i + 0.1
        print(Back.BLUE + f"Compiling C++ [gcc : {i:.2} ms]", end="\r")
        time.sleep(0.1)
    return i

compile_ms = 0
def cmp():
    start = time.time()
    
    # Buat dua thread untuk menjalankan masing-masing fungsi
    thread1 = threading.Thread(target=compile)
    thread2 = threading.Thread(target=dots)

    # Mulai kedua thread
    thread1.start()
    thread2.start()

    # Tunggu hingga kedua thread selesai
    thread1.join()
    compile_ms = thread2.join()
    
    end = time.time()
    return end
    # os.system("cls")

def main():
    # for i in range(10):
    #     dots()
    #     time.sleep(0.5)
    
    c = cmp()
    # float(compile_ms)
    
    arr = sys.argv[1]
    
    
    print()
    printmid("C++", Back.CYAN)
    
    start = time.time()
    os.system(f".\\main {arr} 1 10")
    end = time.time()
    elapsed = end - start
    print(Back.CYAN + f"{elapsed:.2} ms + ({c:.2} ms compile)")
    # printmid(f"{elapsed:.2} ms", Back.CYAN)
    # os.system("pause")
    
    print()
    
    printmid("Python 3.11", Back.YELLOW)
    start = time.time()
    os.system(f"py main.py {arr} 1 10")
    end = time.time()
    elapsed = end - start
    print('\n' + Back.YELLOW + f"{elapsed:.2} ms")
    # printmid(f"{elapsed:.2} ms", Back.YELLOW)
    os.system("pause")
    
main()