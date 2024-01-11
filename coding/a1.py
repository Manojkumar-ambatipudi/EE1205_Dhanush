from sympy import symbols, Sum, simplify
z,n = symbols('z n')
x_n = 36 - 2*n
x_z = sum(x_n*z**(-n),(n,1,13))
print("X(z)=",simplify(x_z))
