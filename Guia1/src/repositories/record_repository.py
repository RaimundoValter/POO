from src.repositories.abstract_repository import AbstractRepository
from src.models.record import Record
from src.utils.file_loader import FileLoader

class RecordRepository(AbstractRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._records = []

    def load_all(self):
        data = FileLoader.load_csv(self._file_path)
        records = []

        for row in data:
            try:
                raw_id = row.get("id", "")
                name = row.get("name", "")
                address = row.get("address", "")

                if raw_id == "" or name.strip() == "" or address.strip() == "":
                    print(f"Registro inválido ignorado: {row}")
                    continue

                record_id = int(raw_id)

                if record_id <= 0:
                    print(f"Registro inválido ignorado: {row}")
                    continue

                records.append(Record(record_id, name, address))

            except (ValueError, TypeError):
                print(f"Registro inválido ignorado: {row}")
                continue

        self._records = records
        return self._records

    def search(self, term: str):
        terms = term.lower().split()
        result = []

        for r in self._records:
            name = r.name.lower()
            address = r.address.lower()

            if all(t in name or t in address for t in terms):
                result.append(r)

        return result