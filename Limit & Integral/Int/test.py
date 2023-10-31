from sympy import symbols, sin, cos, tan, sqrt, pi, integrate

def main():
    x = symbols('x')
    expr = [
        [
            [(2*sin(5*x))],                                 #type: ignore
            [(tan(2*x)**2)],
            [(x*(sin(5*x))/(tan(2*x)**2))]
        ],
        # [
        #     [((sqrt(x + 1) - sqrt(x))**pi)]                 #type: ignore
        # ]
    ]
    
    for n, i in enumerate(expr):
        fx_diff = None
        gx_diff = None
        hx_diff = None
        fx_int = None
        gx_int = None
        hx_int = None
        
        print(f"\nNo. {n+1}")
        print("\nBase: ")
        for id, j in enumerate(i):
            for k in j:
                if id == 1-1:
                    print(f"f(x) = {k}")
                if id == 2-1:
                    print(f"g(x) = {k}")
                if id == 3-1:
                    print(f"H(x) = {k}")
        
        print("\nIntegrate: ")
        for id, j in enumerate(i):
            for k in j:
                if id == 0:
                    fx_int = integrate(k, x)
                    print(f"f(x) = {fx_int}")
                if id == 1:
                    gx_int = integrate(k, x)
                    print(f"g(x) = {gx_int}")
                if id == 2:
                    hx_int = integrate(k, x)
                    print(f"H(x) = {hx_int}")

main()
