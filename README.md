
# 42 Madrid - Exam Rank 03 Python

Repositorio de preparación para el **Exam Rank 03 de Python de 42 Madrid**.

Contiene soluciones de referencia y ejemplos de prueba para los ejercicios del examen. La idea es tener en un solo sitio los patrones más habituales para resolverlos rápido durante la práctica.

## Contenido

- [Estructura del repositorio](#estructura-del-repositorio)
- [Ejercicios](#ejercicios)
- [Uso](#uso)
- [Casos a comprobar](#casos-a-comprobar)
- [Objetivo](#objetivo)

## Estructura del repositorio

```text
exam3/
├── ex1/
│   ├── py_array_rotation_detector.py
│   └── py_constellation_mapper.py
├── ex2/
│   ├── py_list_intersection_finder.py
│   └── py_merge_sorted_lists.py
├── ex3/
│   ├── py_palindrome_partitioner.py
│   └── py_package_dependency_resolver.py
├── ex4/
│   └── py_sliding_window_maximum.py
└── README.md
```

## Ejercicios

### Ejercicio 1

**py_array_rotation_detector** comprueba si una lista es una rotación circular de otra, hacia la izquierda o hacia la derecha.

```python
array_rotation_detector([1, 2, 3], [3, 1, 2])  # True
array_rotation_detector([1, 2, 3], [3, 2, 1])  # False
array_rotation_detector([], [])                # True
```

**py_constellation_mapper** representa estrellas en una cuadrícula utilizando `*` para las estrellas y `.` para las posiciones vacías. Ignora coordenadas fuera de los límites y admite coordenadas repetidas.

```python
constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
# ['*..', '.*.', '..*']
```

### Ejercicio 2

**py_list_intersection_finder** encuentra los elementos comunes a todas las listas ordenadas, eliminando duplicados y manteniendo el orden ascendente.

```python
list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])
# [2, 3]
```

**py_merge_sorted_lists** combina varias listas ordenadas en una única lista ascendente, conservando todos los elementos repetidos.

```python
merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
# [1, 2, 3, 4, 5, 6]
```

### Ejercicio 3

**py_palindrome_partitioner** calcula el número mínimo de cortes necesarios para dividir una cadena en subcadenas que sean palíndromos.

```python
palindrome_partitioner("aab")  # 1
palindrome_partitioner("aba")  # 0
palindrome_partitioner("abc")  # 2
```

**py_package_dependency_resolver** determina un orden válido de instalación de paquetes utilizando sus dependencias. Devuelve una lista vacía si existen dependencias circulares.

```python
package_dependency_resolver({
    "app": ["database"],
    "database": ["driver"],
    "driver": []
})
# ['driver', 'database', 'app']
```

### Ejercicio 4

**py_sliding_window_maximum** encuentra el valor máximo de cada ventana deslizante de tamaño `k` en una lista de números.

```python
sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
# [3, 3, 5, 5, 6, 7]
```

## Uso

Cada solución puede probarse importándola desde otro archivo.

```python
from ex1.py_array_rotation_detector import array_rotation_detector

print(array_rotation_detector([1, 2, 3], [3, 1, 2]))
# True
```

También se pueden añadir pruebas al final de cada archivo para ejecutarlo directamente.

```python
if __name__ == "__main__":
    print(array_rotation_detector([1, 2, 3], [3, 1, 2]))
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
```

Para ejecutar el archivo:

```bash
python3 ex1/py_array_rotation_detector.py
```

Durante el examen, respetar siempre el nombre del archivo, la firma de la función y las restricciones del enunciado. No incluir pruebas adicionales en la entrega salvo que se soliciten.

## Restricciones de la Moulinette

Cada ejercicio puede tener restricciones específicas sobre funciones y módulos permitidos.

- `py_array_rotation_detector`: prohibido `collections.deque.rotate()`.
- `py_constellation_mapper`: ninguna función incorporada permitida.
- `py_list_intersection_finder`: ninguna función incorporada permitida.
- `py_merge_sorted_lists`: prohibidos `sorted()`, `.sort()` y `heapq.merge()`.
- `py_palindrome_partitioner`: ninguna función incorporada permitida.
- `py_package_dependency_resolver`: prohibido `graphlib.TopologicalSorter`.
- `py_sliding_window_maximum`: ninguna función incorporada permitida.

## Casos a comprobar

Conviene probar, como mínimo:

- Entradas vacías.
- Un único elemento.
- Elementos repetidos.
- Números negativos y cero.
- Listas de diferentes tamaños.
- Coordenadas fuera de los límites.
- Cadenas que ya son palíndromos.
- Dependencias circulares y paquetes inexistentes.
- Valores inválidos de `k`.
- Entradas ya ordenadas.
- Casos válidos e inválidos.

## Patrones importantes

Los ejercicios permiten practicar diferentes técnicas habituales en Python:

- **Rotaciones:** slicing y concatenación de listas.
- **Matrices:** bucles anidados y coordenadas.
- **Intersecciones:** búsqueda de elementos comunes.
- **Fusión ordenada:** estructuras heap y combinación de listas.
- **Palíndromos:** programación dinámica.
- **Dependencias:** ordenación topológica.
- **Ventanas deslizantes:** cola monótona.

## Objetivo

El objetivo del repositorio es practicar los patrones de resolución más comunes del examen, aprender soluciones sencillas y funcionales, y poder identificar rápidamente qué técnica aplicar en cada ejercicio.

Se priorizan la claridad del código, el cumplimiento de las restricciones de la Moulinette y el tratamiento correcto de los casos límite.
