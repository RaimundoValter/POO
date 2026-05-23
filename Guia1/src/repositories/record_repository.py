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
                record_id = int(row["id"])
                if record_id <= 0:
                    continue
            except:
                continue
            name = row["name"].strip()
            address = row["address"].strip()
            if not name or not address:
                continue
            self._records.append(Record(record_id, name, address))
        return self._records

    def search(self, termo: str):
        acentos = {'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a'}

        def sem_acento(texto):
            texto = texto.lower()
            for acentuado, letra_simples in acentos.items():
                texto = texto.replace(acentuado, letra_simples)
            return texto

        termos = sem_acento(termo).split()
        results = []
        for registro in self._records:
            found = True
            for t in termos:
                if t not in sem_acento(registro.name) and t not in sem_acento(registro.address):
                    found = False
                    break
            if found:
                results.append(registro)
        return results