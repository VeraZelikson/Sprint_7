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

    @allure.title('Логин несуществующего курьера')
    def test_login_not_existed_courier(self):
        payload = PayloadBuilder.make_courier_create_payload()
        response = ApiService.login_courier(payload)
        assert response.status_code == 404 and response.json() == ExpectedResponses.LOGIN_NOT_EXISTED_RESPONSE

    @allure.title('Логин курьера с неверным паролем')
    def test_login_courier_wrong_password(self):
        payload = PayloadBuilder.make_courier_create_payload()
        response = ApiService.create_courier(payload)
        assert response.status_code == 201
        payload['password'] = 'wrong'
        response = ApiService.login_courier(payload)
        assert response.status_code == 404 and response.json() == ExpectedResponses.LOGIN_NOT_EXISTED_RESPONSE


    @pytest.mark.parametrize(
        'empty_field',
        [
            'login',
            'password'
        ]
    )
    @allure.title('Логин курьера без обязательного поля')
    def test_login_courier_without_required_field(self, empty_field):
        payload = PayloadBuilder.make_courier_create_payload()
        ApiService.create_courier(payload)
        payload[empty_field] = ''
        response = ApiService.login_courier(payload)
        assert response.status_code == 400 and response.json() == ExpectedResponses.LOGIN_NOT_ENOUGH_DATA_RESPONSE
