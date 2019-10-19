import core.generic
from enum import Enum

class BuildingType(Enum):
    INDEPENDENT=1
    APARTMENT=2
    HOTEL=3
    UNKNOWN=4

class Building(generic.Structure):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = None
        self.type = BuildingType.UNKNOWN
        self.details = None

