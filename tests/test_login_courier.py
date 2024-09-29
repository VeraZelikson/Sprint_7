import pytest
import allure

from helpers.api_service import ApiService
from helpers.expexted_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder


class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    def test_login_courier_successfully(self):
        payload = PayloadBuilder.make_courier_create_payload()
        response = ApiService.create_courier(payload)
        assert response.status_code == 201
        response = ApiService.login_courier(payload)
        assert response.status_code == 200 and response.json()['id'] is not None

    # @pytest.mark.parametrize(
    #     'payload',
    #     [
    #         PayloadBuilder.make_courier_create_payload(with_login=False),
    #         PayloadBuilder.make_courier_create_payload(with_password=False),
    #         PayloadBuilder.make_courier_create_payload(with_login=False, with_password=False)
    #     ]
    # )
    # @allure.title('Создание курьера с отсутствием хотя бы одного из обязательных полей')
    # def test_create_courier_successfully(self, payload):
    #     response = requests.post(url=Urls.COURIER_CREATING_URL, data=payload)
    #     assert response.status_code == 400 and response.json() == ExpectedResponses.BAD_DATA_RESPONSE
