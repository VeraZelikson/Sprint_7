import allure

from helpers.api_service import ApiService


class TestOrderList:
    @allure.title('Получение списка последних двух доступных заказов')
    def test_get_order_list(self):
        query = {
            'limit': 2,
            'page': 0
        }
        response = ApiService.order_list(query=query)
        assert response.status_code == 200 and response.json()['orders'] is not None

