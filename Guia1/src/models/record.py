class Record:
    def __init__(self, record_id: int, name: str, address: str):
        self._id = record_id
        self._name = name
        self._address = address

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def __repr__(self):
        return f"Record(id={self._id}, name='{self._name}', address='{self._address}')"