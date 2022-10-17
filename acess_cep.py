import requests


class Search_adress:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("Cep é inválido")

    def __str__(self):
        return self.format_cep()

    def cep_is_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def access_way_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        print(url)
        r = requests.get(url)
        details = r.json()
        return (
            details['bairro'],
            details['localidade'],
            details['uf'],
            details['logradouro']
        )