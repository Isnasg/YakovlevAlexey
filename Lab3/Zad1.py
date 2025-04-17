import pytest
from freezegun import freeze_time
from Lab2/Zad4 import app, weekdays_tuple

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_correct_weekday_response(client):
    test_cases = [
        ('2023-01-02', 'понедельника'),
        ('2023-01-03', 'вторника'),
        ('2023-01-04', 'среды'),
        ('2023-01-05', 'четверга'),
        ('2023-01-06', 'пятницы'),
        ('2023-01-07', 'субботы'),
        ('2023-01-08', 'воскресенья'),
    ]

    for date, expected_day in test_cases:
        with freeze_time(date):
            response = client.get('/Иван')
            assert response.data.decode('utf-8') == f"Привет, Иван. Хорошего {expected_day}!"

def test_good_day_wish_in_username(client):
    with freeze_time('2023-01-02'):
        test_cases = [
            'Хорошего понедельника',
            'Хорошей среды',
            'Прекрасной пятницы',
        ]
        for name in test_cases:
            response = client.get(f'/{name}')
            assert response.data.decode('utf-8') == f"Привет, {name}. Хорошего дня!"

def test_regular_username(client):
    with freeze_time('2023-01-02'):  # Понедельник
        response = client.get('/Алексей')
        assert response.data.decode('utf-8') == "Привет, Алексей. Хорошего понедельника!"