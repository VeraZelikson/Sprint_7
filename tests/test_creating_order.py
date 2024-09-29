import pytest
import allure
from helpers.api_service import ApiService
from helpers.payload_builder import PayloadBuilder


class TestCreatingOrder:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize(
        'scooter_color',
        [
            [],
            ['BLACK', 'GREY'],
            ['BLACK'],
            ['GREY']
        ]
    )
    def test_successful_order(self, scooter_color):
        payload = PayloadBuilder.make_order_payload(scooter_color)
        response = ApiService.create_order(payload)
        assert response.status_code == 201 and response.json()['track'] is not None
