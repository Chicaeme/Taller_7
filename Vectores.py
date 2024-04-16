import numpy as np

# Definimos una matriz cuadrada con valores
A = np.array([[2, 1],
              [1, 3]])

# Calculamos los valores propios y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(A)

# Imprimimos los valores propios y vectores propios
print("Valores propios:")
for value in eigenvalues:
    print(value)

print("\nVectores propios:")
for vector in eigenvectors.T:
    print(vector)
    

#ENLACE EXPLICACIÓN DE VALORES PROPIOS Y VECTORES PROPIOS EN ICG -> https://docs.google.com/document/d/18IANa2-H6eWNWCNhbeOolLb1W97TsgRyx98lZdZrdF0/edit 