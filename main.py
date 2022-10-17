from telephones import TelephonesBr
from acess_cep import Search_adress
from cpf_cnpj import Document
from datesbr import Datas

cep = "07096080"
object_cep = Search_adress(cep)

bairro, cidade, uf, logradouro = object_cep.access_way_cep()

print(bairro, cidade, uf, logradouro)

