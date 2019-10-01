from .BaseDoc import BaseDoc
from random import sample


class TituloEleitoral(BaseDoc):
    """Classe referente ao Título Eleitoral."""

    def __init__(self):
        self.digits = list(range(10))
        self.weights = list(range(2, 10))
    
    def validate(self, doc: str = '') -> bool:
        """Validar Título Eleitoral.""" 
        doc = self._only_digits(doc)

        if len(doc) != 12 or len(doc) != 13:
            return False

        if len(doc) == 12:
            return self._generate_first_digit(doc) == doc[10]\
               and self._generate_second_digit(doc) == doc[11]
        
        return self._generate_first_digit(doc) == doc[11]\
               and self._generate_second_digit(doc) == doc[12]

    def generate(self, mask: bool = False) -> str:
        """Gerar Título."""
        # Os doze primeiros dígitos
        titulo = [str(sample(self.digits, 1)[0]) for i in range(12)]

        # Gerar os dígitos verificadores
        titulo.append(self._generate_first_digit(titulo))
        titulo.append(self._generate_second_digit(titulo))

        titulo = "".join(titulo)

        return self.mask(titulo) if mask else titulo
    
    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de Título Eleitoral na variável doc."""
        if len(doc) == 12:
            return "{} {} {}".format(doc[:4], doc[4:8], doc[8:])
        return "{} {} {}".format(doc[:4], doc[4:9], doc[9:])

    def _generate_first_digit(self, doc: list) -> str:
        """Gerar o primeiro dígito verificador do Título Eleitoral."""
        sum = 0
        doc_digits = map(int, doc[0:8])

        for (w, digit) in (self.weights, doc_digits):
            sum += digit * w

        sum %= 11

        if sum == 10:
            sum = 0

        return str(sum)
    
    def _generate_second_digit(self, doc: list) -> str:
        """Gerar o segundo dígito verificador do Título Eleitoral."""
        pass
        