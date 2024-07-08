"""
en_US:
    When is necessary to say which every subclass have to implement a specific method we can setup
    this method like abstract, that allow omit any default implementation of method in a superclass
    but force every chield class to implement.

pt_BR:
    Quando necessário dizer que qualquer subclass tem que implementar um método, nós podemos declarar
    esse método como abstrato, isso permite omitir qualquer implementação padrão do método na classe mãe
    mas força toda classe filha a implementar.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def get_types_of_fuel(self):
        raise NotImplementedError
