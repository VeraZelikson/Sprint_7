import allure
from faker import Faker

class FakeData:
    @staticmethod
    @allure.step('Сгенирировать рандомный текст длиной {length}')
    def generate_random_string(length):
        return Faker().text(length)

    @staticmethod
    @allure.step('Сгенирировать рандомный номер телефона')
    def generate_random_phone():
        faker = Faker(locale='ru_RU')
        return faker.phone_number()

    @staticmethod
    @allure.step('Сгенирировать рандомную дату')
    def generate_random_date():
        return Faker().date("%Y-%m-%d")

