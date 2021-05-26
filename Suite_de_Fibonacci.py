# Ecrire une fonction récursive permettant de calculer le n ième terme de la suite de Fibonacci.
#fonction fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n<=2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
# faire une fonction dans une fonction : récurssivité

a = fibonacci(int(input("valeur de n = ")))
print(a)