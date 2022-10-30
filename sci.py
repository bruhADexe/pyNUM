from scipy import constants
print(constants.liter)
import scipy
print(scipy.__version__)
print(constants.pi)
print(dir(constants))
print(constants.Avogadro)
print(constants.Boltzmann)
print(constants.kibi)
print(constants.kilo)
print(constants.ounce)
print("Roots of an equation")
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)
print(myroot.x)
print(myroot)

# minima of a function
print("Mininma of a function")
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin =  minimize(eqn, 0, method='BFGS')
print(mymin)

print("sparse Data")
# prints the raw num and index of non zero
from scipy.sparse import csr_matrix
import numpy as np
arr = np.array([1, 2, 0, 0, 5, 0, 7])
print(csr_matrix(arr))

print("this will print non zero element i.e. actual data")
arr = np.array([[0,0], [2,0], [0, 3], [0, 1]])
print(csr_matrix(arr).data)

print("this will count all the non zero entries")
print(csr_matrix(arr).count_nonzero())

print("this will remove all the zero entries")
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

print("this will remove all the duplicate entries(eliminates duplicate by adding them)")
mat.sum_duplicates()
print(mat)

print("To convert CSR to CSC(compressed sparse column)")

arrr = csr_matrix(arr).tocsc()
print(arrr)




