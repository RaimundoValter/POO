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
                novo_registro = Record(row["id"], row["name"], row["address"])
                self._records.append(novo_registro)
            except ValueError:
                print(f"Registro inválido ignorado: {{'id': '{row['id']}', 'name': '{row['name']}', 'address': '{row['address']}'}}")
                continue
            
        return self._records

    def search(self, term: str):
        term_lista = term.lower().split()

        if not term_lista:
            return []

        resultados = []
        
        for r in self._records:
            palavras_do_registro = r.name.lower().split() + r.address.lower().split()
            print(f'{palavras_do_registro}')
            contem_todos = True
            for palavra in term_lista:
                if palavra not in palavras_do_registro:
                    contem_todos = False
                    break
            
            if contem_todos:
                resultados.append(r)

        return resultados