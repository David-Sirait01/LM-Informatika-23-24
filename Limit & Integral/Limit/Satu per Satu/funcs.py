from sympy import symbols, diff, limit, sin, cos, tan, latex, pi, oo, sqrt, solve
from math import pi as mth_pi
from pyfiglet import figlet_format

# def detectos():
#     import platform as p
#     os = p.system()
#     os_v = None
#     if os == 'Windows':
#         os_v = 1
#     elif os == 'Linux':
#         os_v = 2

def pause_py():
    input("Press Enter to continue...")

def withlim(expr, x):
    return str("\\lim_{x\\rightarrow") + (f"{latex(x)}}}") + '\n\t' + str(latex(expr))

def writeto(file, content):
    with open(f"{file}", "a+") as fl:
        fl.write(content+"")
        
def body():
    x = symbols('x')
    a = symbols('a')
    def no1():
        expr = (x * sin(5*x))/tan(2*x)**2
        close_to = 0
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.1\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
    no1()

    def no2():
        expr = (12*x-4*x**2)/(sin(4*x))
        close_to = 0
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.2\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no2()

    def no3():
        expr = (cos(7*x)-cos(3*x))/(cos(4*x)-1)
        close_to = 0
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.3\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no3()

    def no4():
        expr = (1-sin(6*x))/(cos(6*x)**2)
        close_to = pi/12
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.4\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no4()

    def no5():
        expr = (3*cos(x)**2 - sin(x)**2 - sin(2*x))/(cos(x)**2+sin(x)*cos(x)-2*sin(x)**2)
        close_to = pi/4
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.5\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no5()

    def no6():
        expr = ((2+3*x)*(1-x**2))/((x+5)*(x**2)+3)
        close_to = oo
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.6\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no6()
    
    def no7():
        expr = (tan(3/x)+sin(7/x))/(sin(8/x)-tan(3/x))
        close_to = oo
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.7\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no7()

    def no8():
        expr = sqrt(9*x**2 - 12*x + 4) - 3*x - 1
        close_to = oo
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.8\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no8()

    def no9():
        x, a = symbols('x a')
        
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

        content = f"No.9\t{withlim(expr, oo)}\n\n\tResult = {a_inverse_square}\n\tlatex = {latex(a_inverse_square)}\n"
        print(content)
        writeto("eq.txt", content)
        
    no9()

    def no10():
        expr = (6*(x**2-9)*tan(x**2-6*x+9))/((3*x-x**2)*sin(2*x-6)**2)
        close_to = 3
        result = limit(expr, x, close_to)
        result_latX = latex(result)
        content = f"No.10\t{withlim(expr, close_to)}\n\n\tResult = {result}\n\tlatex = {result_latX}\n"
        print(content)
        writeto("eq.txt", content)
        
    no10()