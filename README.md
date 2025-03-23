# Simulación de Monte Carlo en Finanzas

## Problema 1: Estimación de la raíz cuadrada de 3

### Problema
Se quiere estimar el valor de \( \sqrt{3} \) mediante simulación de Monte Carlo.

### Solución en Python
```python
from random import random 
import matplotlib.pyplot as plt 
from math import sqrt 

N = 10000000 
n = 0 
lx = [] 
ly = [] 
lsqrt = [] 

for i in range(N): 
    x = 1 + random() 
    if x**2 < 3: 
        n += 1 
        if i % 10000 == 0 and i > 0: 
            lx.append(i) 
            ly.append(n/i + 1) 
            lsqrt.append(sqrt(3)) 

plt.plot(lx, ly) 
plt.plot(lx, lsqrt) 
plt.xlabel("Número de iteraciones") 
plt.ylabel("Aproximación de \(\sqrt{3}\)") 
plt.grid() 
plt.legend(["Aproximación de \(\sqrt{3}\)", "\(\sqrt{3}\)"]) 
plt.title("Aproximación de \(\sqrt{3}\) por simulación") 
plt.show() 

print(n/N + 1)
```

---

## Problema 2: Estimación del volumen de una esfera de radio 1

### Problema
Estimar el volumen de una esfera de radio 1 utilizando el método de Monte Carlo.

### Solución en Python
```python
from random import random 
N = 10000000 
n = 0 

for i in range(N): 
    x = random() 
    y = random() 
    z = random() 
    if x**2 + y**2 + z**2 < 1: 
        n += 1 

V = 8 * (n / N)  # Volumen dentro del cubo
print(f"El volumen de la esfera, calculado por simulación es: V={V}")
```

---

## Problema 3: Estimación del valor esperado de una variable aleatoria

### Problema
Se define una variable aleatoria \( N \) como el mínimo número de variables uniformemente distribuidas en \([0,1]\) tal que su suma sea mayor a 1. Se desea estimar \( E(N) \).

### Solución en Python
```python
N = 100000 
s = 0 

for i in range(N):
    suma = 0
    contador = 0
    while suma < 1:
        suma += random()
        contador += 1
    s += contador

E_N = s / N
print(f"Valor esperado estimado: {E_N}")
```

---

## Problema 4: Estimación de integrales

### Problema
Estimar el valor de varias integrales mediante simulación de Monte Carlo.

### Solución en Python
```python
from math import exp, sqrt, sin
N = 1000000 

integral1 = sum(sqrt(1 + random()**3) for _ in range(N)) / N
integral2 = sum(exp(-(3 + (5 - 3) * random())**2) * (5 - 3) for _ in range(N)) / N
integral3 = sum(sin(0.5 + (1 - 0.5) * random()) / (0.5 + (1 - 0.5) * random()) * (1 - 0.5) for _ in range(N)) / N

print(f"El valor de la primera integral es: {integral1}")
print(f"El valor de la segunda integral es: {integral2}")
print(f"El valor de la tercera integral es: {integral3}")
```

---

## Problema 5: Estimación del valor esperado de una variable geométrica

### Problema
Estimar el valor esperado de una variable aleatoria geométrica con parámetro \( p \) y dar un intervalo de confianza del 95%.

### Solución en Python
```python
from math import log, sqrt

def geometrica(p):
    u = random()
    return int(log(1 - u) / log(1 - p)) + 1

N = 100000
p = 0.2
s = 0
var = 0
valores = []

for i in range(N):
    x = geometrica(p)
    s += x
    valores.append(x)

media = s / N
varianza = sum((x - media)**2 for x in valores) / (N - 1)
intervalo_confianza = (media - 1.96 * sqrt(varianza / N), media + 1.96 * sqrt(varianza / N))

print(f"Valor esperado estimado: {media}")
print(f"Intervalo de confianza al 95%: {intervalo_confianza}")
```

---

## Problema 6: Estimación del máximo de variables uniformes

### Problema
Sean \( U_1, U_2, ..., U_{10} \) variables aleatorias independientes y uniformemente distribuidas en \([0,1]\). Se desea estimar el valor esperado del máximo de estas variables.

### Solución en Python
```python
N = 100000
M = 0

for i in range(N):
    M += max(random() for _ in range(10))

E_M = M / N
print(f"Valor esperado estimado: {E_M}")
```

---

## Problema 7: Estimación del valor esperado de una variable con distribución especial

### Problema
Sean \( X_1, X_2, ..., X_5 \) variables con densidad de probabilidad \( f(x) = 2x \) para \( x \in [0,1] \). Se desea estimar el valor esperado de \( g(X) = X^2 \).

### Solución en Python
```python
N = 100000
s = 0

for i in range(N):
    x = sqrt(random())  # Inversa de la CDF de f(x)
    s += x**2

E_X2 = s / N
print(f"Valor esperado estimado: {E_X2}")
```

---
