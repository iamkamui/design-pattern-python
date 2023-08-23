"""
Considere o cenário de uma aplicação de viagem de Carro, pode haver diversos
contextos diferentes. No primeiro caso ele guarda detalhes relacionados ao
veículo, enquanto no segundo se importaria somente com quantidade de assentos
disponíveis.
"""


class Carro1:
    def __init__(self, modelo, motor, ano, cor):
        self.modelo = modelo
        self.motor = motor
        self.ano = ano
        self.cor = cor

    def trip(self):
        print("Triping...")


class Carro2:
    def __init__(self, seats):
        self.seats = seats

    def reserve_seats(self):
        print("Reserving seats...")
