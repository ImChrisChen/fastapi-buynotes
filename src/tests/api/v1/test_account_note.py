from fastapi.testclient import TestClient

from main import app
from src.config.config import settings

client = TestClient(app)

BASE_URL = settings.API_V1_STR


def test_app():
    r = client.get(f'{BASE_URL}')
    response = r.json()
    assert response['code'] == 0


# def test_get_account_types():
#     r = client.get(f'{BASE_URL}/account_type')
#     response = r.json()
#     print('response:', response)
#     assert response['code'] == 0
#     assert type(response['data']) == list
#
#
# def test_create_account_type():
#     data = {"amount_type": "0", "type_zh_name": "服装", "type_en_name": "clothing"}
#     r = client.post(
#         f'{BASE_URL}/account_type',
#         headers={'Content-Type': 'application/json'},
#         json=data
#     )
#     response = r.json()
#
#     print(response)
#
#     assert response['code'] == 0
#     assert response['data']['type_zh_name'] == data['type_zh_name']
#     assert response['data']['type_en_name'] == data['type_en_name']
#     assert response['data']['amount_type'] == data['amount_type']
