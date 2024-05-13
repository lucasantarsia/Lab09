from dataclasses import dataclass

@dataclass
class Airport:
    _id: int
    _iata_code: str
    _airport: str
    _city: str
    _state: str
    _country: str
    _latitude: float
    _longitude: float
    _timezone_offset: float

    @property
    def id(self):
        return self._id

    @property
    def iata_code(self):
        return self._iata_code

    @property
    def airport(self):
        return self._airport

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def country(self):
        return self._country

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def timezone_offset(self):
        return self._timezone_offset

    def __hash__(self):
        return hash(self._id)
