import random

from faker import Faker

from data import TestData


class GenerateTestData:
    faker = Faker('ru_RU')

    def create_register_information(self):
        # генерируем почту, пароль и имя
        email = self.faker.email()
        password = self.faker.password()
        name = self.faker.first_name()

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    def bun(self):
        selected_bun = random.choice(TestData.buns_id)
        return selected_bun

    def sauce(self):
        selected_sauce = random.choice(TestData.sauces_id)
        return selected_sauce

    def filling(self):
        selected_filling = random.choice(TestData.fillings_id)
        return selected_filling