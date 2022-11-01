# Operaciones-con-Conjuntos
Programa realizado como parte de las actividades semanales de la cátedra 2011 de la materia Estructura de Datos, de la carrera Ingeniería en Computación de la Universidad Nacional de Tres de Febrero.

## Consigna

Se necesita poder realizar todas las operaciones posibles entre conjuntos.

Para ello se pide implementar la clase Conjunto (utilizando listas de Python), con métodos para cada una de las siguientes operaciones:

* Unión
* Intersección
* Diferencia
* Diferencia simétrica
* Producto cartesiano

Las operaciones deben retornar un Conjunto con los elementos resultantes. La operación de producto cartesiano deberá retornar un conjunto de tuplas.

Además un conjunto debe:

* permitir crear un conjunto vacío.
* permitir crear un conjunto en base a una lista de elementos.
* permitir agregar un elemento a si mismo.
* permitir remover un elemento contenido en él.
* tener la habilidad de compararse con otro conjunto.

Se deberá proveer código que muestre el uso de los distintos métodos. Por ejemplo:

a = Conjunto([1, 2, 3, 4, 5])

b = Conjunto([3, 4, 5, 6, 7])

c = a.union(b)
c == Conjunto([1, 2, 3, 4, 5, 6, 7]) # => True

**Importante**: la característica principal de los conjuntos es que **no contiene elementos duplicados**.
