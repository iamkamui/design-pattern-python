"""
en_US:
    If you want to create new classes with a bit diferents that one that already exists,
    don't have necessity to duplicate your code, you can extends the existent class and create
    the adicional funcionality inside of subclass.

pt_BR:
    Se você deseja criar novas classes um pouco diferentes daquela que já existe,
    não há necessidade de duplicar seu código, você pode estender a classe existente e criar
    a funcionalidade adicional dentro da subclasse.
"""

from typing import Dict


class RoadTransport:
    def __init__(self, model: str, engine: str, year: str, color: str):
        self.model = model
        self.engine = engine
        self.year = year
        self.color = color

    def start_engine(self) -> str:
        return f"Starting {self.engine} engine ..."

    def _base_info(self) -> Dict:
        return {
            "model": self.model,
            "engine": self.engine,
            "year": self.year,
            "color": self.color,
        }


class Motorcyle(RoadTransport):
    def __init__(self, lever_type: str, model: str, engine: str, year: str, color: str):
        super().__init__(model, engine, year, color)
        self.lever_type = lever_type

    def wheelie(self) -> str:
        return "Wheeling..."

    def get_bike_info(self) -> Dict:
        base_info = self._base_info()
        base_info.update({"lever_type": self.lever_type})
        return base_info


class Car(RoadTransport):
    def __init__(self, body: str, model: str, engine: str, year: str, color: str):
        super().__init__(model, engine, year, color)
        self.body = body

    def get_car_info(self) -> Dict:
        base_info = self._base_info()
        base_info.update({"body": self.body})
        return base_info
