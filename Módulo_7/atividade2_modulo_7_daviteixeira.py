'''

Instale e utilize uma biblioteca externa (faker, datetime, etc.).

Escolha uma biblioteca externa, como faker para gerar dados falsos ou datetime para trabalhar com datas
e implemente um programa que utilize essa biblioteca para resolver um problema prático.

'''

from faker import Faker

fake = Faker("pt_BR")

for _ in range(3):
    print("Nome:", fake.name())
    print("Email:", fake.email())
    print("Endereço:", fake.address())
    print("-" * 30)
