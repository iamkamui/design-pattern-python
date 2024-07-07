"""
en_US:
    Consider the scene of car travel application, where can have a lot of diferents context.
    In the first case, the class save data related of car, althrouth in the second, what metter
    is the quantity of avialable seats.

pt_BR:
    Considere o cenário de uma aplicação de viagem de Carro, pode haver diversos
    contextos diferentes. No primeiro caso ele guarda detalhes relacionados ao
    veículo, enquanto no segundo se importaria somente com quantidade de assentos
    disponíveis.
"""


class Car:
    def __init__(self, model: str, engine: str, year: str, color: str):
        self.model = model
        self.engine = engine
        self.year = year
        self.color = color

    def trip(self) -> str:
        return "Triping..."


class Car2:
    def __init__(self, seats: str):
        self.seats = seats

    def reserve_seats(self) -> str:
        return "Reserving seats..."
