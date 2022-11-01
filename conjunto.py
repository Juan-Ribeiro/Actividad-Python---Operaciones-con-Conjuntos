class Conjunto:
    def __init__(self, elementos=[]):
        """Crea un Conjunto de elementos a partir de una lista de elementos dada
        Permite crear un Conjunto vacio
        :param elementos: una lista de elementos
        """
        self.conjunto = []
        for elemento in elementos:
            self.agregar_elemento(elemento)

    def agregar_elemento(self, elemento):
        """Agrega un elemento al conjunto, si ya no lo contiene

        :param elemento: un elemento
        """
        if elemento not in self.conjunto:
            self.conjunto.append(elemento)

    def eliminar_elemento(self, elemento):
        """Elimina un elemento existente del conjunto

        :param elemento: un elemento
        """
        if elemento in self.conjunto:
            self.conjunto.remove(elemento)

    def devolver_conjunto(self):
        return self.conjunto

    def union(self, other):
        """Realiza la operacion 'union' junto a otro Conjunto.

        Devuelve un Conjunto compuesto por todos los elementos de 'self' y 'other'.

        :param other: otro Conjunto
        :return: tipo Conjunto
        """
        return Conjunto(self.conjunto + [x for x in other.devolver_conjunto() if x not in self.conjunto])

    def interseccion(self, other):
        """Realiza la operacion 'interseccion' junto a otro Conjunto.

        Devuelve un Conjunto cuyos elementos coincidan en 'self' como en 'other'.

        :param other: otro Conjunto
        :return: tipo Conjunto
        """
        resultante = Conjunto()
        for elemento in self.conjunto:
            if elemento in other.conjunto:
                resultante.agregar_elemento(elemento)
        return Conjunto([x for x in other.devolver_conjunto() if x in self.conjunto])

    def diferencia(self, other):
        """Realiza la operacion 'diferencia' a partir de otro Conjunto.

        Devuelve un Conjunto semejante a 'self' excluyendo los elementos
        repetidos en 'other'.

        :param other: otro Conjunto
        :return: tipo Conjunto
        """
        resultante = Conjunto()
        for elemento in self.conjunto:
            if not other.conjunto.__contains__(elemento):
                resultante.agregar_elemento(elemento)
        return resultante

    def diferencia_simetrica(self, other):
        """ Realiza la operacion 'diferencia simetrica' a partir de otro Conjunto.

        Devuelve un Conjunto que contenga solo los elementos que no se repiten en
        ambos Conjuntos ('self' y 'other').

        :param other: otro Conjunto
        :return: tipo Conjunto
        """
        resultante = Conjunto()

        for elemento in self.conjunto:
            if not other.conjunto.__contains__(elemento):
                resultante.agregar_elemento(elemento)

        for elemento in other.conjunto:
            if not self.conjunto.__contains__(elemento):
                resultante.agregar_elemento(elemento)

        return resultante

    def producto_cartesiano(self, other):
        """ Calcula el producto cartesiano con respecto a otro Conjunto

        Devuelve una Tupla compuesta de n-Tuplas, a su vez compuestas de pares ordenados
        entre cada elemento de ambos Conjuntos

        :param other: otro Conjunto
        :return: tipo Tupla
        """
        resultante = ()
        for elemento_self in self.conjunto:
            tupla = ()
            for elemento_other in other.conjunto:
                tuplita = (elemento_self, elemento_other),
                tupla += tuplita
            resultante += tupla,
        return resultante

    def __eq__(self, other):
        """Devuelve si dos Conjuntos son iguales o no a partir de sus elementos.

        :param other: otro Conjunto
        """
        for elemento in self.conjunto:
            if elemento not in other.devolver_conjunto():
                return False

        for elemento in other.devolver_conjunto():
            if elemento not in self.conjunto:
                return False

        return True

    def __repr__(self):
        return self.conjunto


# Probando metodos de operaciones entre conjuntos

# Probando crear conjuntos (incluyendo uno vacio)
print("Probando creacion de conjuntos..")
a = Conjunto([1, 2, 3, 4, 5])
b = Conjunto([3, 4, 5, 6, 7])

print(a)
print(b)
print()

# Probando eliminar elemento en conjunto
print("Probando eliminar elemento..")
a.eliminar_elemento(5)
print(a.conjunto)
print()

# Probando agregar elemento en conjunto
print("Probando agregar elemento..")
a.agregar_elemento(5)
print(a.conjunto)
print()

# Probando metodo 'union'
print("Probando metodo 'union'..")
c = a.union(b)
print(c.conjunto)
print(c == Conjunto([1, 2, 3, 4, 5, 6, 7]))
print()

# Probando metodo 'interseccion'
print("Probando metodo 'interseccion'..")
d = a.interseccion(b)
print(d.conjunto)
print(d == Conjunto([3, 4, 5]))
print()

# Probando metodo 'diferencia'
print("Probando metodo 'diferencia'..")
e = a.diferencia(b)
print(e.conjunto)
print(e == Conjunto([1, 2]))
print()

# Probando metodo 'diferencia_simetrica'
print("Probando metodo 'diferencia_simetrica'..")
f = a.diferencia_simetrica(b)
print(f.conjunto)
print(f == Conjunto([1, 2, 6, 7]))
print()

# Probando metodo 'producto_cartesiano' (devuelve tuplas concatenadas)
print("Probando metodo 'producto_cartesiano'..")
g = a.producto_cartesiano(b)
print(g)
print(g == (((1, 3), (1, 4), (1, 5), (1, 6), (1, 7)), ((2, 3), (2, 4), (2, 5), (2, 6), (2, 7)),
            ((3, 3), (3, 4), (3, 5), (3, 6), (3, 7)), ((4, 3), (4, 4), (4, 5), (4, 6), (4, 7)),
            ((5, 3), (5, 4), (5, 5), (5, 6), (5, 7))))
print(type(g) is tuple)
