import generic


class Building(generic.Structure):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = None
        self.details = None

