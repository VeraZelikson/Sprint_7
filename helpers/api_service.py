import requests

from helpers.payload_builder import PayloadBuilder
from helpers.urls import Urls


class ApiService:
    @staticmethod
    def create_courier(payload=PayloadBuilder.make_courier_create_payload()):
        return requests.post(url=Urls.COURIER_CREATING_URL, data=payload)

    @staticmethod
    def login_courier(payload):
        requests.post(url=Urls.COURIER_LOGIN_URL, data=payload)
