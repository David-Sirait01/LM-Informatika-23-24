/*

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


        ...
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
        0, 0, ...
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


*/

#include <ginac/ginac.h>
#include <iostream>

int main() {
    using namespace GiNaC;

    // Membuat simbol-simbol
    symbol x("x");
    
    // Membuat ekspresi matematika simbolik
    ex expression = sin(x) * cos(x);

    // Menghitung turunan pertama terhadap x
    ex derivative = diff(expression, x);

    // Cetak hasil turunan
    std::cout << "Ekspresi: " << expression << std::endl;
    std::cout << "Turunan pertama: " << derivative << std::endl;

    return 0;
}