'''
Kondisional : Jumat 25 Agustus 2023
'''
import sys

def main():
    var = sys.argv[1]
    
    a = int(var)
    #a = int(input("Enter a value : "))
    if a%2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")


if __name__ == "__main__":
    import time
    # Record the start time
    start_time = time.time()
    
    main()

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = (end_time - start_time) * 1000
    print(f"\n\nExecution time: {elapsed_time:.2f} ms")