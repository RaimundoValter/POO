from src.repositories.abstract_repository import AbstractRepository
from src.models.record import Record
from src.utils.file_loader import FileLoader

class RecordRepository(AbstractRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._records = []

    def load_all(self):
        data = FileLoader.load_csv(self._file_path)
        self._records = []
        
        for row in data:
            try:
                if not row.get("id"):
                    raise ValueError("ID vazio")

                record_id = int(row["id"])

                if record_id <= 0:
                    raise ValueError("ID negativo ou zero")

                if not row.get("name", "").strip() or not row.get("address", "").strip():
                    raise ValueError("Nome ou endereço vazio")

                registro = Record(record_id, row["name"], row["address"])
                self._records.append(registro)
                
            except ValueError:
                print(f"Registro inválido ignorado: {row}")
                
        return self._records

    def search(self, term: str):
        termos_busca = term.lower().split()
        
        return [
            r for r in self._records
            if all(t in f"{r.name} {r.address}".lower() for t in termos_busca)
        ]
  