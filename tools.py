from random import randint

def multiply(x,y):
    return x * y

def addition(a,b):
    return a + b

def syracuse(n):
    if n%2==0:
        return n//2
    return 3 * n + 1

def rand_cell():
    return (randint(0,19),randint(0,19))

if '__name__'=='__main__':
    print('ceci est le fichier outils')