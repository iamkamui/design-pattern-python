"""
en_US:
    Using encapsulation we can restric one class and be certain that only objects
    that implement the specific interface which the class needs, can woking on.

pt_BR:
    Usando encapsulamento nós podemos restrigir uma classe e ter certeza que somente objetos
    que implementam uma interface especifica que a classe necessita, pode trabalhar com ela.
"""

from ._inheritance import RoadTransport


class Highway:

    def can_travel_through(vehicle: RoadTransport) -> bool:
        return isinstance(vehicle, RoadTransport)
