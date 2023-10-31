from sympy import symbols, sin, tan, cos, limit, sqrt, sympify, pi, oo, latex, solve
from pyfiglet import figlet_format

# Mendefinisikan simbol-simbol yang diperlukan
x, a = symbols('x a')

def withlim(expr, x):
    return str("\\lim_{x\\rightarrow") + (f"{latex(x)}}}") + "\n\t" + str(latex(expr))
    #                                                 ^^
    #                                   Using double }} to print an actual '}'

def writeto(file, content):
    with open(f"{file}", "a+") as fl:
        fl.write(content+"")

def main():
    fig = figlet_format("Latihan Soal")
    print(fig)
    writeto("eq2.txt", fig)

    
    expr = [
        # Dummy supaya index[0] ga diikut sertakan
        (1),

        # No.1
        ((x * sin(5*x))/(tan(2*x)**2)),
        
        # No.2
        ((12*x-4*x**2)/sin(4*x)),
        
        # No.3
        ((cos(7*x) - cos(3*x)) / (cos(4*x) - 1)),
        
        # No.4
        ((1 - sin(6*x))/(cos(6*x)**2)),
        
        # No.6
        ((5*x**2-10*x)/(sin(2*x)**2)),

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

        print(f"No.9\t{withlim(expr, oo)}\n\n\tResult = {a_inverse_square}\n\tlatex = {latex(a_inverse_square)}\n")

    # X mendekati ...
    close_to_values = [
        # No 1 - 6
        0, 0, 0, pi/12, 0, 0,

        # No 7 - 13, (!12)
        pi/4, 0, oo, oo, oo, oo, 3
    ]
    
    for i in range(1, len(expr)):
        if i == 12:
            no12()
        elif i != 12:
            result = limit(expr[i], x, close_to_values[i])
            content = f"{i + 1}.\t{withlim(expr[i], close_to_values[i])}\n\n\tResult = {result}\n\tLaTeX = {latex(result)}\n"
            print(content)
            writeto("eq2.txt", content)


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

    input("Press Enter to continue...")
