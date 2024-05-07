from dataclasses import dataclass


@dataclass
class Airport:
    _id: int
    _name: str
    _city: str
    _state: str
    _coutry: str

    def __str__(self):
        return f"id: {self._id} airport: {self._name}"

    def __repr__(self):
        return f"id: {self._id} airport: {self._name}"

    def __hash__(self):
        return hash(self._id)
