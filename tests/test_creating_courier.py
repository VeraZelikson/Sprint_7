import pytest
import allure

from helpers.api_service import ApiService
from helpers.expexted_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder


class TestCreatingCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_successfully(self):
        response = ApiService.create_courier()
        assert response.status_code == 201 and response.json() == ExpectedResponses.SUCCESS_RESPONSE

    @allure.title('Создание курьера с тем же логином')
    def test_create_courier_duplicated(self):
        payload = PayloadBuilder.make_courier_create_payload()
        ApiService.create_courier(payload)
        response = ApiService.create_courier(payload)
        assert response.status_code == 409 and response.json() == ExpectedResponses.DUPLICATED_COURIER_RESPONSE

    @allure.title('Создание курьера только с обязательными полями')
    def test_create_courier_required_fields(self):
        payload = PayloadBuilder.make_courier_create_payload(with_first_name=False)
        response = ApiService.create_courier(payload)
        assert response.status_code == 201 and response.json() == ExpectedResponses.SUCCESS_RESPONSE

    @pytest.mark.parametrize(
        'payload',
        [
            PayloadBuilder.make_courier_create_payload(with_login=False),
            PayloadBuilder.make_courier_create_payload(with_password=False),
            PayloadBuilder.make_courier_create_payload(with_login=False, with_password=False)
        ]
    )
    @allure.title('Создание курьера с отсутствием хотя бы одного из обязательных полей')
    def test_create_courier_without_required_field(self, payload):
        response = ApiService.create_courier(payload)
        assert response.status_code == 400 and response.json() == ExpectedResponses.BAD_DATA_RESPONSE
