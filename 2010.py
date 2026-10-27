#SISTEMAS LINEARES
import numpy as np 

A = np.array([[10, 7, 8, 7],
              [7, 5, 6, 5],
              [8, 6, 10, 9],
              [7, 5, 9, 10]])

B = np.array([32, 23, 33, 31])

x = np.dot(np.linalg.inv(A), B)
print(x)

#REGRESSÃO LINEAR
y = [0, 0, 2, 3, 4, 4, 5, 6, 8, 8]
X = [[1, -2], [1, -2], [1, -1], [1, -1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 2], [1, 2]]

#beta = (X'X)^-1 X'*y
Xt = np.transpose(X) #X'
XtX = np.dot(Xt, X) #(X'X)
XtXinv= np.linalg.inv(XtX) #(X'X)^-1
Xty = np.dot(Xt, y)

beta = np.dot(XtXinv, Xty)
print(beta)

#OUTRO MODO DE ADICIONAR O 1 NO X
#X = [-2, -2, -1, -1, 0, 0, 1, 1, 2, 2]
#X_new = [[1, i] for i in X]
#print(X_new)