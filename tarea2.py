def bubble_sort_fila(fila):
  """Ordena una fila de una matriz utilizando el algoritmo Bubble Sort.

  Args:
    fila: La lista que representa una fila de la matriz.
  """

  n = len(fila)
  for i in range(n):
    for j in range(0, n-i-1):
      if fila[j] > fila[j+1]:
        fila[j], fila[j+1] = fila[j+1], fila[j]

# Matriz bidimensional de 3x3
matriz = [[3, 1, 2],
          [5, 4, 6],
          [9, 8, 7]]

# Aplicar Bubble Sort a cada fila
for fila in matriz:
  bubble_sort_fila(fila)

print(matriz)

