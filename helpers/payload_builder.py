from helpers.fakedata import FakeData
import random


class PayloadBuilder:
    @staticmethod
    def make_courier_create_payload(with_login=True, with_password=True, with_first_name=True):
        payload = {}
        if with_login:
            payload["login"] = FakeData.generate_random_string(10)
        if with_password:
            payload["password"] = FakeData.generate_random_string(10)
        if with_first_name:
            payload["firstName"] = FakeData.generate_random_string(10)
        return payload

    @staticmethod
    def make_login_payload(login, password):
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password
        return payload

    @staticmethod
    def make_order_payload(scooter_colors):
        payload = {
            "firstName": FakeData.generate_random_string(10),
            "lastName": FakeData.generate_random_string(10),
            "address": FakeData.generate_random_string(10),
            "metroStation": random.randint(1, 268),
            "phone": FakeData.generate_random_phone(),
            "rentTime": random.randint(1, 12),
            "deliveryDate": FakeData.generate_random_date(),
            "comment": FakeData.generate_random_string(10),
            "color": scooter_colors
        }
        return payload
