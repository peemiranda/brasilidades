from validate_docbr import CNPJ
from validate_docbr import CPF


class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpf(document)

        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Quantidade de digitos esta incorreta!!")


class DocCpf(Document):
    def __init__(self, document):
        if self.valid(document):
            self.cpf = document
        else:
            raise ValueError("Cpf inválido")

    def __str__(self):
        return self.format()

    def valid(self, document):
        validate = CPF()
        return validate.validate(document)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)


class DocCnpj(Document):
    def __init__(self, document):
        if self.valid(document):
            self.cnpj = document
        else:
            raise ValueError("Cnpj inválido")

    def __str__(self):
        return self.format()

    def valid(self, document):
        mask = CNPJ()
        return mask.validate(document)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

