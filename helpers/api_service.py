import allure
import requests

from helpers.payload_builder import PayloadBuilder
from helpers.urls import Urls


class ApiService:

    @staticmethod
    @allure.step('Создать курьера payload = {payload}')
    def create_courier(payload=PayloadBuilder.make_courier_create_payload()):
        return requests.post(url=Urls.COURIER_CREATING_URL, data=payload)

    @staticmethod
    @allure.step('Залогинить курьера payload = {payload}')
    def login_courier(payload):
        return requests.post(url=Urls.COURIER_LOGIN_URL, data=payload)

    @staticmethod
    @allure.step('Создать заказ payload = {payload}')
    def create_order(payload):
        return requests.post(url=Urls.CREATE_ORDER_URL, data=payload)

    @staticmethod
    @allure.step('Получить список доступных заказов query = {query}')
    def order_list(query):
        return requests.get(url=Urls.ORDER_LIST_URL, params=query)
