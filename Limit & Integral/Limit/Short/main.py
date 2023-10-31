from sympy import symbols, sin, tan, cos, limit, pi, oo, latex

def main():
    def limnote(expr, n):
        r"""Expr and n must be a pure expr"""
        lat = r"\lim_{x \rightarrow " + str(latex(n)) + r"} " + latex(expr)
        return str(lat)
    
    x = symbols('x')
    # expr =  ((x * sin(5*x))/(tan(2*x)**2))
    # n = 0
    
    # result = limit(expr, x, n)
    # print(f"{expr}, n = {n} = {result}")
    
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
    ]
    
    n = [
        None,                   # 0th index
        0, 0, 0, pi/12, 0, 0,   # Actual n value
    ]
    
    for i in range(1, 6):
        result = limit(expr[i], x, n[i])
        # print(f"No.{i} {expr[i]}, n = {n[i]} = {result}")
        # print(f"\\text{{No.{i}}} {latex(expr[i])}, n = {latex(n[i])} = {latex(result)} \\\\")
        print(f"\\text{{No.{i}}}\t {limnote(expr[i], n[i])} = {latex(result)}" + "\\\\")
        
main()