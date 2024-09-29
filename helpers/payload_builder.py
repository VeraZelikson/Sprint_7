from helpers.faker import Faker


class PayloadBuilder:
    @staticmethod
    def make_courier_create_payload(with_login=True, with_password=True, with_first_name=True):
        payload = {}
        if with_login:
            payload["login"] = Faker.generate_random_string(10)
        if with_password:
            payload["password"] = Faker.generate_random_string(10)
        if with_first_name:
            payload["firstName"] = Faker.generate_random_string(10)
        return payload

    @staticmethod
    def make_login_payload(login, password):
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password
        return payload
