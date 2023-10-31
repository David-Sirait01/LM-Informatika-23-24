# from sympy import symbols, tan, Integral
# from sympy.printing import latex
# from IPython.display import display, Latex
# x = symbols("x")

# def print_line(x):
#     tx = []
#     for i in range(x):
#         tx.append("-")
#     return "".join(tx)

# def main():
#     # tx = []
#     # for i in range(4):
#     #     tx.append("-")
        
#     # x = "".join(tx)

#     # print(x)
#     gx = tan(2*x)**2
#     print(f"\n{gx}\n{print_line(len(str(gx)))}")

# def main():
    # x = symbols('x')
    # expr = (5*x**4 - 8*x**3 + 7*x) / (5*x**2 + 9*x)

    # # Mendapatkan ekspresi dalam format LaTeX
    # latex_expr = latex(Integral(expr, x))

    # # Menampilkan persamaan dalam format LaTeX
    # display(Latex(latex_expr))
    # import platform as p
    # arr = [
    #     p.architecture(),
    #     p.freedesktop_os_release(),
    #     p.java_ver(),
    #     p.libc_ver()
    # ]

import platform as p

def main():
    arr = [
        p.architecture(),
        # p.freedesktop_os_release(),
        p.java_ver(),
        p.libc_ver(),
        p.machine(),
        p.node(),
        p.platform(),
        p.processor(),
        p.python_branch()
    ]

    print(arr)


if __name__ == "__main__":
    main()