import statistics as st
import numpy as np
from colorama import init, Fore

from sympy import symbols, sin, cos, tan, limit, oo
x = symbols("x")
    
def simpangan_baku(arr):
    return np.std(arr)
    
def main():
    init(autoreset=True)
    arr = [28, 30, 22, 24, 26, 20, 23, 20]
    mean = st.mean(arr)
    median = st.median(arr)
    modus = st.mode(arr)
    
    print(f"arr = {arr}\nmean = {mean}\nmedian = {median}\nmodus = {modus}")
    print(f"\n{Fore.GREEN} simpangan baku = {simpangan_baku(arr)}")

def main2():
    expr = (3-3*cos(6*x))/(2*tan(3*x)**2)
    result = limit(expr, x, 0)
    print(f"expr = {expr}\nresult = {result}")
    
def main3():
    expr = (3/2)*x - (2*x**3 + 2*x**2 + 4)/((2*x - 1)**2)
    result = limit(expr, x, oo)
    print(f"expr = {expr}\nresult = {result}")

def main4():
    expr = 4*x**2 * (cos(5/x)-1)
    result = limit(expr, x, oo)
    print(f"expr = {expr}\nresult = {result}")
    
main4()