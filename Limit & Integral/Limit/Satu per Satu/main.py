from funcs import *

def main():
    fig = figlet_format("Latihan Soal")
    print(fig)
    writeto("eq.txt", fig)
    body()

if __name__ == "__main__":
    import time
    # Record the start time
    start_time = time.time()
    
    main()

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = (end_time - start_time) * 1000
    print(f"Execution time: {elapsed_time:.2f} ms")

    pause_py()