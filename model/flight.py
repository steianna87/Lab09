from dataclasses import dataclass
from datetime import datetime


@dataclass
class Flight:
    _id: int
    _airline_id: int
    _flight_number: int
    _tail_number: str
    _origin_airport_id: int
    _destination_airport_id: int
    _scheduled_departure_date: datetime
    _departure_delay: float
    _elapsed_time: float
    _distance: int
    _arrival_date: datetime
    _arrival_delay: float

    def __str__(self):
        return f"ID: {self._id} DISTANCE: {self._distance}"

    def __repr__(self):
        return f"id: {self._id} distance: {self._distance}"


