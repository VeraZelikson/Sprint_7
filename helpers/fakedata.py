from faker import Faker

class FakeData:
    @staticmethod
    def generate_random_string(length):
        return Faker().text(length)

    @staticmethod
    def generate_random_phone():
        faker = Faker(locale='ru_RU')
        return faker.phone_number()

    @staticmethod
    def generate_random_date():
        return Faker().date("%Y-%m-%d")

