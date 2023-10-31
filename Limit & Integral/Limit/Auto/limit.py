from sympy import symbols, sin, tan, cos, limit, sqrt, sympify, pi, oo, latex, solve

def withlim(expr, x):
    return str("\\lim_{x\\rightarrow") + (f"{latex(x)}}}") + "\n\t" + str(latex(expr))
    #                                                 ^^
    #                                   Using double }} to print an actual '}'

def writeto(file, content):
    with open(f"{file}", "a+") as fl:
        fl.write(content+"")

def main():
    banner = " _     _           _ _   \n| |   (_)_ __ ___ (_) |_ \n| |   | | '_ ` _ \\| | __|\n| |___| | | | | | | | |_ \n|_____|_|_| |_| |_|_|\\__|\n                         \n _____     _                                        _        _ \n|_   _| __(_) __ _  ___  _ __   ___  _ __ ___   ___| |_ _ __(_)\n  | || '__| |/ _` |/ _ \\| '_ \\ / _ \\| '_ ` _ \\ / _ \\ __| '__| |\n  | || |  | | (_| | (_) | | | | (_) | | | | | |  __/ |_| |  | |\n  |_||_|  |_|\\__, |\\___/|_| |_|\\___/|_| |_| |_|\\___|\\__|_|  |_|\n             |___/                                             \n"
    
    with open("eq2.txt", "a") as f:
        f.truncate(0)

    # Generated using pyfiglet.figlet_format("Limit Trigonometri")
    writeto("eq2.txt", f"{banner}\n")
    print(banner)
    x = symbols('x')
    expr = [
        # Dummy supaya index[0] ga diikut sertakan
        (1),

        # No.1
        ((x * sin(5*x))/(tan(2*x)**2)),
        
        # No.2
        ((12*x-4*x**2)/sin(4*x)),
        
        # No.3
        ((cos(7*x) - cos(3*x))) / ((cos(4*x) - 1)),
        
        # No.4
        ((1 - sin(6*x))/(cos(6*x)**2)),

        # No. 5
        (x * tan(6*x))/(sin(2*x)**2),
        
        # No.6
        ((5*x**2-10*x)/(sin(5*x))),

        # No.7
        (3*cos(x)**2 - sin(x)**2 - sin(2*x))/(cos(x)**2+sin(x)*cos(x)-2*sin(x)**2),

        # No.8
        ((cos(6*x)-cos(3*x))/(cos(6*x)-1)),
        
        # No.9
        ((2+3*x)*(1-x**2))/((x+5)*(x**2)+3),
        
        # No.10
        (tan(3/x)+sin(7/x))/(sin(8/x)-tan(3/x)),
        
        # No.11
        (sqrt(9*x**2 - 12*x + 4) - 3*x - 1),

        # No.12 (Dummy doang)
        (1),
        
        # No.13
        (6*(x**2-9)*tan(x**2-6*x+9))/((3*x-x**2)*sin(2*x-6)**2)
    ]

    def no12():
        # Define symbols
        x, a = symbols('x a')
        
        # Define the expression
        expr = ((a*x - 3)**5) / (8*x**5 + 5*x**3 + 2*x - 1)
        
        # Calculate the limit as x approaches infinity
        limit_result = limit(expr, x, oo)
        
        # Set the limit_result equal to 4
        limit_eq = limit_result - 4
        
        # Solve for a^(-2)
        solution = solve(limit_eq, a)
        
        # Print the solution
        if solution:
            a_inverse_square = solution[0]**(-2)
            # print(f'a^(-2) = {a_inverse_square}')
        else:
            print("No solution found.")

        return f"No.12\t{withlim(expr, oo)}\n\n\tResult = {a_inverse_square}\n\tlatex = {latex(a_inverse_square)}\n"


    # X mendekati ...
    close_to_values = [
        0,
        # No 1 - 6
        0, 0, 0, pi/12, 0, 0,

        # No 7 - 13, (!12)
        pi/4, 0, oo, oo, oo, 1, 3
    ]
    
    # Latex only
    # latX = []

    # print(len(expr))
    print()
    for i in range(1, len(expr)):
        if i == 12:
            content = no12()
            print(content)
            writeto("eq2.txt", content + "\n")
            # latX.append(content)
        elif i != 12:
            result = limit(expr[i], x, close_to_values[i])
            # latX.append(withlim(expr[i], close_to_values[i]))
            content = f"No {i}.\t{withlim(expr[i], close_to_values[i])}={latex(result)}\n\n\tResult = {result}\n\tLaTeX = {latex(result)}\n"
            print(content)
            writeto("eq2.txt", f"{content}\n")
    
    # for i in range(1, len(expr)):
    #     writeto("eq2.txt", latX[i])

if __name__ == "__main__":
    import time, os
    # Record the start time
    start_time = time.time()
    
    main()

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = (end_time - start_time) * 1000
    print(f"Execution time: {elapsed_time:.2f} ms")

    os.system("pause")
    # input("Press Enter to continue...")

'''
\\A.\\
1. f(x) = \sin(2x) \rightarrow f'(x)=2\cos(2x)\\
2. f(x) = \cos(3x) \rightarrow f'(x)=-3\sin(3x)\\
3. f(x) = \tan(4x) \rightarrow f'(x)=4\sec^2(4x)\\
4. f(x) = \sin(x^2) \rightarrow f'(x)=2x\cos(x^2)\\
5. f(x) = \cos(2x^3)\rightarrow f'(x)= -6x\sin(2x^3)\\\\

B.\\
1. f(x)=\sin(2x+3) \rightarrow f'(x)=\cos(2x+3).2\\
2. f(x)=\cos(3x-1) \rightarrow f'(x)=-\sin(3x-1).3\\
3. f(x)=\tan(4x+2) \rightarrow f'(x)=\sec^2(4x+2).4\\
4. f(x)=\sin(2x^2+3x+1) \rightarrow f'(x)=\cos(2x^2+3x+1).(4x+3)\\
5. f(x)=\cos(3x^2-2x-1) \rightarrow f'(x)=-\sin(3x^2-2x+1).(6x-2)\\\\

C.\\
1. f(x)=\sin^3(2x+1) \rightarrow f'(x)=(6x+6)sin^2(2x+1).\cos(2x+1)\\
2. f(x)=\cos^4(3x-2) \rightarrow f'(x)=(-21x+4)cos^3(3x-2).\sin(3x-2)\\
3. f(x)=\tan^2(4x+3) \rightarrow f'(x)=(8x+6)\tan(4x+3).\sec^2(4x+3)\\
4. f(x)=\sin^5(2x^2+3x+1) \rightarrow f'(x)=(10x^2 + 15x + 5)\sin^4(2x^2+3x+1).\cos(2x^2+3x+1)\\
5. f(x)=\cos^3(3x^2-2x-1) \rightarrow f'(x)=(-9x^2 + 6x + 3)\cos^2(3x^2-2x-1).\sin(3x^2-2x-1)
'''