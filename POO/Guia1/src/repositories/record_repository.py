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
        term = term.lower()
        # Quebra a busca do usuário em uma lista de termos individuais
        # Ex: "joao rua a" vira ['joao', 'rua', 'a']
        term_lista = term.split()

        # Se o usuário não digitou nada, retorna uma lista vazia
        if not term_lista:
            return []

        resultados = []

        for r in self._records:
            # Juntamos o nome e o endereço em letras minúsculas para a busca
            palavras_do_registro = r.name.lower().split() + r.address.lower().split()
            
            # Começamos assumindo que este registro contém todas as palavras
            contem_todos = True
            
            # Testamos palavra por palavra da busca do usuário
            for palavra in term_lista:
                if palavra not in palavras_do_registro:
                    # Se APENAS UMA palavra não for encontrada, o registro não serve
                    contem_todos = False
                    break # Interrompe o loop das palavras para economizar processamento
            
            # Se o loop terminou e a bandeira continuou True, o registro passou no teste!
            if contem_todos:
                resultados.append(r)

        return resultados

