def even(arr, opt=1):
    ret = [i for i in arr if i%2 == 0]
    if opt==1:
        return len(ret)
    elif opt == 2:
        return ret

def odd(arr, opt=1):
    ret = [i for i in arr if i%2 != 0]
    if opt==1:
        return len(ret)
    elif opt == 2:
        return ret
            
def main():
    import random, time as tm, sys
    ln = int(sys.argv[1])
    lb = int(sys.argv[2])
    ub = int(sys.argv[3])
    
    arr = []
    for i in range(ln):
        if KeyboardInterrupt:
            pass
        
        t = random.randint(lb, ub)
        print(f"Enter value[{i}] : {t}", end="\r")
        # tm.sleep(0.1)
        
        # t = input(f"Enter value[{i}] : ")
        arr.append(t)
    
    # reverse
    print(f"Original : {arr}")
    arr.reverse()
    print(f"\nReversed : {arr}")
    
    # odd && even
    arr.reverse()
    print(f"odd  : {odd(arr, opt=2)}")
    print(f"even : {even(arr, opt=2)}")
    
    # odd && even count
    print(f"odd count : {odd(arr, opt=1)}")
    print(f"even count: {even(arr, opt=1)}")
    
    # avg
    print(f"Average = {sum(arr)/len(arr)}")
  
main()  
# if __name__ == "__main__":
#     import time
#     # Record the start time
#     start_time = time.time()
    
#     main()

#     # Record the end time
#     end_time = time.time()

#     # Calculate the elapsed time
#     elapsed_time = (end_time - start_time) * 1000
#     print(f"Execution time: {elapsed_time:.2f} ms")