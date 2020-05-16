from sympy import *
a = Matrix ([[1,2,3], [2,3,4], [5,6,7]])
print(a)
L, U , _= a.LUdecomposition ()
print (L)
print (U)
