import numpy as np

def calculate_svd(A):
    AT = A.transpose()
    print(f"A^T:= {AT}")
    ATA = np.dot(AT, A)
    print(f"A^T * A := {ATA}")
    ew = np.linalg.eigvals(ATA)
    print(f"Eigenwerte := {ew}")
    sig = np.sqrt(ew)
    print(f"Singulärwerte := {sig}")
    return sig

def calculate_cross(a, b):
    print(np.cross(a, b))

def euler_phi(n):
    """Berechnet die Eulersche Phi-Funktion phi(n)"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    print(result)
    return result

def calculate_determinant(A):
    det = np.linalg.det(A)
    print(f"Determinante := {det}")
    return det

def inverse_matrix(A):
    inv_A = np.linalg.inv(A)
    print(f"Inverse Matrix := {inv_A}")
    return inv_A

if __name__ == '__main__':
    A = np.array([[3,3,3], [3,2,2], [3,2,1]])
    inverse_matrix(A)